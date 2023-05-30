DELIMITER //

CREATE PROCEDURE AtualizarQuantidadeProduto(
  IN p_produto_id INT,
  IN p_quantidade_vendida INT
)
BEGIN
  UPDATE Produtos
  SET quantidade = quantidade - p_quantidade_vendida
  WHERE id = p_produto_id;
END //

CREATE PROCEDURE RealizarVenda (
  IN p_id_cliente INT,            -- ID do cliente associado à venda
  IN p_id_vendedor INT,           -- ID do vendedor responsável pela venda
  IN p_data_venda DATE,           -- Data da venda
  IN p_produtos VARCHAR(255),     -- IDs dos produtos separados por vírgula
  IN p_quantidades VARCHAR(255)   -- Quantidades dos produtos separadas por vírgula
)
BEGIN
  DECLARE total DECIMAL(10, 2);   -- Variável para armazenar o valor total da venda
  DECLARE id_venda INT;           -- Variável para armazenar o ID da venda

  -- Inserir nova venda na tabela Venda
  INSERT INTO Venda (id_cliente, id_vendedor, data_venda, valor_total)
  VALUES (p_id_cliente, p_id_vendedor, p_data_venda, 0);

  -- Obter o ID da venda inserida
  SET id_venda = LAST_INSERT_ID();

  -- Calcular o valor total da venda
  SET total = 0;

  -- Drop the temporary table if it exists
  DROP TEMPORARY TABLE IF EXISTS temp_produto_quantidade;

  -- Create the temporary table
  CREATE TEMPORARY TABLE temp_produto_quantidade (
    id_produto INT,
    quantidade INT
  );

  -- Insert the product IDs and quantities into the temporary table
  SET @sql = CONCAT('INSERT INTO temp_produto_quantidade (id_produto, quantidade) VALUES ');
  SET @products = REPLACE(p_produtos, ' ', ''); -- Remove spaces from the product string
  SET @quantities = REPLACE(p_quantidades, ' ', ''); -- Remove spaces from the quantity string
  SET @delimiter = ',';
  SET @product_count = LENGTH(REPLACE(@products, ',', ''));
  SET @i = 1;

  WHILE @i <= @product_count DO
    SET @product_id = SUBSTRING_INDEX(SUBSTRING_INDEX(@products, @delimiter, @i), @delimiter, -1);
    SET @quantity = SUBSTRING_INDEX(SUBSTRING_INDEX(@quantities, @delimiter, @i), @delimiter, -1);
    -- Montar a query de inserção dos detalhes da venda
    IF @i > 1 THEN
      SET @sql = CONCAT(@sql, ', ');
    END IF;
    SET @sql = CONCAT(@sql, '(', @product_id, ', ', @quantity, ')');

    SET @i = @i + 1;
  END WHILE;

  PREPARE stmt FROM @sql;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;

  -- Calcular o valor total da venda usando a tabela temporária
  SET @sql = CONCAT('SELECT SUM(p.valor_unitario * tpq.quantidade) INTO @total FROM Produtos p JOIN temp_produto_quantidade tpq ON p.id = tpq.id_produto');
  PREPARE stmt FROM @sql;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;

  -- Atualizar o valor total da venda na tabela Venda
  UPDATE Venda SET valor_total = @total WHERE id = id_venda;

  -- Inserir os detalhes da venda na tabela DetalhesVenda
  SET @sql = CONCAT('INSERT INTO DetalhesVenda (id_venda, id_produto, quantidade_vendida, valor_unitario) SELECT ', id_venda, ', tpq.id_produto, tpq.quantidade, p.valor_unitario FROM temp_produto_quantidade tpq JOIN Produtos p ON p.id = tpq.id_produto');
  PREPARE stmt FROM @sql;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;

  -- Drop the temporary table
  DROP TEMPORARY TABLE IF EXISTS temp_produto_quantidade;
END //

CREATE PROCEDURE ObterDetalhesVenda(IN venda_id INT)
BEGIN
  SELECT
    c.nome AS "Nome do Cliente",
    c.email AS "E-mail do Cliente",
    c.celular AS "Celular do Cliente",
    dv.quantidade AS "Quantidade do Item",
    p.descricao AS "Descrição do Produto",
    p.valor_unitario AS "Valor do Produto",
    (dv.quantidade * p.valor_unitario) AS "Subtotal do Item",
    v.valor_total AS "Valor Total da Compra"
  FROM Venda v
  JOIN Cliente c ON v.id_cliente = c.id
  JOIN DetalhesVenda dv ON v.id = dv.id_venda
  JOIN Produtos p ON dv.id_produto = p.id
  WHERE v.id = venda_id;
END //

CREATE PROCEDURE ObterRelatorioVendas(IN vendedor_id INT)
BEGIN
  DECLARE vendedor_nome VARCHAR(100);
  DECLARE vendedor_email VARCHAR(100);
  DECLARE vendedor_telefone VARCHAR(20);
  DECLARE mes INT;
  DECLARE total_vendas DECIMAL(10, 2);
  DECLARE total_comissao DECIMAL(10, 2);

  -- Cursor para percorrer as vendas do vendedor
  DECLARE vendas_cursor CURSOR FOR
    SELECT MONTH(data_venda), valor_total, comissao
    FROM Venda
    WHERE id_vendedor = vendedor_id;

  -- Variável temporária para armazenar os resultados de cada venda
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET @finished = 1;

  -- Verificar e excluir a tabela temporária existente
  IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'RelatorioVendas') THEN
    DROP TABLE RelatorioVendas;
  END IF;

  -- Criação da tabela temporária para armazenar o relatório
  CREATE TEMPORARY TABLE RelatorioVendas (
    vendedor_nome VARCHAR(100),
    vendedor_email VARCHAR(100),
    vendedor_telefone VARCHAR(20),
    mes INT,
    total_vendas DECIMAL(10, 2),
    total_comissao DECIMAL(10, 2)
  );

  -- Obter os dados do vendedor
  SELECT nome, email, telefone INTO vendedor_nome, vendedor_email, vendedor_telefone
  FROM Vendedores
  WHERE id = vendedor_id;

  SET total_vendas = 0;
  SET total_comissao = 0;

  OPEN vendas_cursor;

  -- Loop pelas vendas do vendedor
  vendas_loop: LOOP
    FETCH vendas_cursor INTO mes, total_vendas, total_comissao;

    IF @finished = 1 THEN
      LEAVE vendas_loop;
    END IF;

    INSERT INTO RelatorioVendas (vendedor_nome, vendedor_email, vendedor_telefone, mes, total_vendas, total_comissao)
    VALUES (vendedor_nome, vendedor_email, vendedor_telefone, mes, total_vendas, total_comissao);
  END LOOP vendas_loop;

  CLOSE vendas_cursor;

  -- Seleção dos resultados formatados
  SELECT
    vendedor_nome AS "Nome do Vendedor",
    vendedor_email AS "E-mail do Vendedor",
    vendedor_telefone AS "Telefone do Vendedor",
    mes AS "Mês",
    total_vendas AS "Valor Total das Vendas",
    total_comissao AS "Valor Total da Comissão"
  FROM RelatorioVendas;

  -- Limpeza da tabela temporária
  DROP TABLE RelatorioVendas;
END //

DELIMITER ;

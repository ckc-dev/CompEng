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

  -- Drop the temporary table if it exists
  DROP TEMPORARY TABLE IF EXISTS temp_produto_quantidade;

  -- Create the temporary table
  CREATE TEMPORARY TABLE temp_produto_quantidade (
    id_produto INT,
    quantidade INT
  );

  -- Inserir nova venda na tabela Venda
  INSERT INTO Venda (id_cliente, id_vendedor, data_venda, valor_total)
  VALUES (p_id_cliente, p_id_vendedor, p_data_venda, 0);

  -- Obter o ID da venda inserida
  SET id_venda = LAST_INSERT_ID();

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
  SET total = (
    SELECT SUM(p.valor_unitario * tpq.quantidade)
    FROM Produtos p
    JOIN temp_produto_quantidade tpq ON p.id = tpq.id_produto
  );

  -- Atualizar o valor total da venda na tabela Venda
  UPDATE Venda SET valor_total = total WHERE id = id_venda;

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
    c.telefone AS "Telefone do Cliente",
    dv.quantidade_vendida AS "Quantidade do Item",
    p.descricao AS "Descrição do Produto",
    p.valor_unitario AS "Valor do Produto",
    (dv.quantidade_vendida * p.valor_unitario) AS "Subtotal do Item",
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
  DECLARE temp_table_name VARCHAR(100) DEFAULT 'RelatorioVendas';

  -- Cursor para percorrer as vendas do vendedor
  DECLARE vendas_cursor CURSOR FOR
    SELECT MONTH(data_venda), SUM(valor_total)
    FROM Venda
    WHERE id_vendedor = vendedor_id
    GROUP BY MONTH(data_venda);

  -- Variável temporária para armazenar os resultados de cada venda
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET @finished = 1;

  -- Verificar e excluir a tabela temporária existente
  SET @sql = CONCAT('DROP TABLE IF EXISTS ', temp_table_name);
  PREPARE stmt FROM @sql;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;

  -- Criação da tabela temporária para armazenar o relatório
  SET @sql = CONCAT('CREATE TEMPORARY TABLE ', temp_table_name, ' (
    vendedor_nome VARCHAR(100),
    vendedor_email VARCHAR(100),
    vendedor_telefone VARCHAR(20),
    mes INT,
    valor_vendas DECIMAL(10, 2),
    valor_comissao DECIMAL(10, 2)
  )');
  PREPARE stmt FROM @sql;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;

  -- Obter os dados do vendedor
  SELECT nome, email, telefone INTO vendedor_nome, vendedor_email, vendedor_telefone
  FROM Vendedores
  WHERE id = vendedor_id;

  SET total_vendas = 0;
  SET total_comissao = 0;
  SET @finished = 0; -- Reset the @finished variable

  OPEN vendas_cursor;

  -- Loop pelas vendas do vendedor
  vendas_loop: LOOP
    FETCH vendas_cursor INTO mes, total_vendas;

    IF @finished = 1 THEN
      LEAVE vendas_loop;
    END IF;

    -- Cálculo da comissão
    SET total_comissao = (
      SELECT SUM(c.valor_comissao)
      FROM Comissoes c
      JOIN Venda v ON c.id_venda = v.id
      WHERE MONTH(v.data_venda) = mes
    );

    SET @sql = CONCAT('INSERT INTO ', temp_table_name, ' (vendedor_nome, vendedor_email, vendedor_telefone, mes, valor_vendas, valor_comissao) VALUES (',
                      QUOTE(vendedor_nome), ', ', QUOTE(vendedor_email), ', ', QUOTE(vendedor_telefone), ', ', mes, ', ', total_vendas, ', ', total_comissao, ')');
    PREPARE stmt FROM @sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
  END LOOP vendas_loop;

  CLOSE vendas_cursor;

  -- Seleção dos resultados formatados
  SET @sql = CONCAT('SELECT
    vendedor_nome AS "Nome do Vendedor",
    vendedor_email AS "E-mail do Vendedor",
    vendedor_telefone AS "Telefone do Vendedor",
    mes AS "Mês",
    SUM(valor_vendas) AS "Valor Total das Vendas",
    SUM(valor_comissao) AS "Valor Total da Comissão"
  FROM ', temp_table_name, '
  GROUP BY vendedor_nome, vendedor_email, vendedor_telefone, mes');

  PREPARE stmt FROM @sql;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;

  -- Limpeza da tabela temporária
  SET @sql = CONCAT('DROP TABLE IF EXISTS ', temp_table_name);
  PREPARE stmt FROM @sql;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;
END //

DELIMITER ;

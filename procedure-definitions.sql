DELIMITER //

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
  -- Consultar o valor unitário dos produtos selecionados e somar o valor total
  SET @sql = CONCAT('SELECT SUM(valor_unitario * quantidade) INTO @total FROM Produtos WHERE id IN (', p_produtos, ')');
  PREPARE stmt FROM @sql;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;

  -- Atualizar o valor total da venda na tabela Venda
  UPDATE Venda SET valor_total = @total WHERE id = id_venda;

  -- Inserir os detalhes da venda na tabela DetalhesVenda
  SET @sql = CONCAT('INSERT INTO DetalhesVenda (id, id_venda, id_produto, quantidade, valor_unitario) VALUES ');
  SET @products = p_produtos;
  SET @quantities = p_quantidades;
  SET @delimiter = ',';
  SET @i = 1;
  WHILE @i <= LENGTH(@products) DO
    SET @product_id = SUBSTRING_INDEX(SUBSTRING_INDEX(@products, @delimiter, @i), @delimiter, -1);
    SET @quantity = SUBSTRING_INDEX(SUBSTRING_INDEX(@quantities, @delimiter, @i), @delimiter, -1);
    -- Montar a query de inserção dos detalhes da venda
    SET @sql = CONCAT(@sql, '(', @i, ', ', id_venda, ', ', @product_id, ', ', @quantity, ', (SELECT valor_unitario FROM Produtos WHERE id = ', @product_id, '))');
    IF @i < LENGTH(@products) THEN
      SET @sql = CONCAT(@sql, ', ');
    END IF;
    SET @i = @i + 1;
  END WHILE;
  PREPARE stmt FROM @sql;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;
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

DELIMITER ;

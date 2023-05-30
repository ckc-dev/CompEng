DELIMITER //

CREATE TRIGGER CriarComissao
AFTER INSERT ON DetalhesVenda
FOR EACH ROW
BEGIN
  DECLARE valor_comissao DECIMAL(10, 2);

  SELECT dv.quantidade_vendida * p.valor_unitario * p.comissao_percentual / 100 INTO valor_comissao
  FROM Produtos p
  JOIN DetalhesVenda dv on p.id = dv.id_produto
  WHERE p.id = NEW.id_produto
  LIMIT 1;

  INSERT INTO Comissoes (id_venda, id_vendedor, id_produto, valor_comissao)
  VALUES (NEW.id_venda, (SELECT id_vendedor FROM Venda WHERE id = NEW.id_venda), NEW.id_produto, valor_comissao);
END //

CREATE TRIGGER AtualizarQuantidadeProdutosPosVenda
AFTER UPDATE ON Venda
FOR EACH ROW
BEGIN
  DECLARE produto_id INT;
  DECLARE quantidade_vendida INT;
  DECLARE done INT DEFAULT FALSE;

  DECLARE cur CURSOR FOR
    SELECT id_produto, quantidade_vendida
    FROM DetalhesVenda
    WHERE id_venda = NEW.id;

  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

  OPEN cur;

  read_loop: LOOP
    FETCH cur INTO produto_id, quantidade_vendida;

    IF done THEN
      LEAVE read_loop;
    END IF;

    CALL AtualizarQuantidadeProduto(produto_id, quantidade_vendida);
  END LOOP;

  CLOSE cur;
END //

DELIMITER ;

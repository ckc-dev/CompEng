DELIMITER //

CREATE TRIGGER CriarComissao
AFTER INSERT ON DetalhesVenda
FOR EACH ROW
BEGIN
  DECLARE valor_comissao DECIMAL(10, 2);

  SELECT valor_unitario * comissao_percentual / 100 INTO valor_comissao
  FROM Produtos
  WHERE id = NEW.id_produto;

  INSERT INTO Comissoes (id_venda, id_vendedor, id_produto, valor_comissao)
  VALUES (NEW.id_venda, (SELECT id_vendedor FROM Venda WHERE id = NEW.id_venda), NEW.id_produto, valor_comissao);
END //

CREATE TRIGGER RemoverEstoque
AFTER INSERT ON DetalhesVenda
FOR EACH ROW
BEGIN
  UPDATE Produtos
  SET quantidade = quantidade - 1
  WHERE id = NEW.id_produto;
END //

DELIMITER ;

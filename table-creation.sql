CREATE DATABASE IF NOT EXISTS vendas;
USE vendas;

CREATE TABLE IF NOT EXISTS Produtos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  descricao VARCHAR(100),
  valor_unitario DECIMAL(10,2),
  comissao_percentual DECIMAL(5,2),
  quantidade INT
);

CREATE TABLE IF NOT EXISTS Cliente (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(100),
  telefone VARCHAR(20),
  email VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Vendedores (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(100),
  telefone VARCHAR(20),
  email VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Venda (
  id INT PRIMARY KEY AUTO_INCREMENT,
  id_cliente INT,
  id_vendedor INT,
  data_venda DATE,
  valor_total DECIMAL(10, 2),
  FOREIGN KEY (id_cliente) REFERENCES Cliente(id),
  FOREIGN KEY (id_vendedor) REFERENCES Vendedores(id)
);

CREATE TABLE IF NOT EXISTS Comissoes (
  id INT PRIMARY KEY AUTO_INCREMENT,
  id_venda INT,
  id_produto INT,
  id_vendedor INT,
  valor_comissao DECIMAL(10, 2),
  FOREIGN KEY (id_venda) REFERENCES Venda(id),
  FOREIGN KEY (id_produto) REFERENCES Produtos(id),
  FOREIGN KEY (id_vendedor) REFERENCES Vendedores(id)
);

CREATE TABLE IF NOT EXISTS DetalhesVenda (
  id INT PRIMARY KEY AUTO_INCREMENT,
  id_venda INT,
  id_produto INT,
  quantidade_vendida INT,
  valor_unitario DECIMAL(10, 2),
  FOREIGN KEY (id_venda) REFERENCES Venda(id),
  FOREIGN KEY (id_produto) REFERENCES Produtos(id)
);

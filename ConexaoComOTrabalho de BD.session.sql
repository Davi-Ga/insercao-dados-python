CREATE TABLE cidade(
    nome VARCHAR(100) NOT NULL,
    regiao VARCHAR(2) NOT NULL,
    uf VARCHAR(2) NOT NULL,
    PRIMARY KEY(nome,uf)
);

CREATE TABLE unidade(
    nome VARCHAR(100) NOT NULL,
    cnpj VARCHAR(100) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    cep VARCHAR(100) NOT NULL,
    id_unidade SERIAL PRIMARY KEY
);

CREATE TABLE pertenceCit_Unid(
    nomeFK VARCHAR(100) NOT NULL,
    ufFK VARCHAR(2) NOT NULL,
    id_unidadeFK INT NOT NULL,
    FOREIGN KEY (nomeFK,ufFK) REFERENCES cidade(nome,uf),
    FOREIGN KEY (id_unidadeFK) REFERENCES unidade(id_unidade)
);

CREATE TABLE produto(
    tipo VARCHAR(30),
    valor_venda DOUBLE PRECISION,
    data_coleta DATE,
    bandeira VARCHAR(100),
    id_produto  SERIAL PRIMARY KEY
);

CREATE TABLE contemProd_Unid(
    id_unidadeFK INT NOT NULL,
    id_produtoFK INT NOT NULL,
    FOREIGN KEY (id_unidadeFK) REFERENCES unidade(id_unidade),
    FOREIGN KEY (id_produtoFK) REFERENCES produto(id_produto)
);
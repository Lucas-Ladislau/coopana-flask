CREATE SCHEMA IF NOT EXISTS coopana;

CREATE TABLE IF NOT EXISTS coopana.produto(
    id SERIAL NOT NULL,
    nome VARCHAR(150) NOT NULL,
    CONSTRAINT pk_produto_id PRIMARY KEY (id)
    );

CREATE TABLE IF NOT EXISTS coopana.cultura(
    id SERIAL NOT NULL,
    produto INT NOT NULL,
    tipo VARCHAR(100),
    valor FLOAT,
    quantidade FLOAT,
    CONSTRAINT pk_cultura_id PRIMARY KEY (id),
    CONSTRAINT fk_cultura_produto FOREIGN KEY (produto)
    REFERENCES coopana.produto (id)
    );

-------------------------------------------------------
--Definir melhor o endereço para propriedades agrícolas
-------------------------------------------------------
CREATE TABLE IF NOT EXISTS coopana.endereco (
    id SERIAL NOT NULL,
    cidade VARCHAR(150) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    CONSTRAINT pk_endereco_id PRIMARY KEY (id)
    );

CREATE TABLE IF NOT EXISTS coopana.cooperado (
    id SERIAL NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    celular VARCHAR(20) NULL,
    cultura INT NOT NULL,
    endereço INT NOT NULL,
    CONSTRAINT pk_cooperado_id PRIMARY KEY (id),
    CONSTRAINT fk_cultura_id FOREIGN KEY (cultura)
    REFERENCES coopana.cultura (id),
    CONSTRAINT fk_endereco_id FOREIGN KEY (endereco)
    REFERENCES coopana.endereco (id)
    );


CREATE TABLE IF NOT EXISTS coopana.licitação (
    id SERIAL NOT NULL,
    financiador VARCHAR(255) NOT NULL,
    licitacao_destino VARCHAR(255) NOT NULL,
    CONSTRAINT pk_licitacao_id PRIMARY KEY (id)
    );

CREATE TABLE IF NOT EXISTS coopana.projeto (
    id SERIAL NOT NULL,
    nome VARCHAR(255) NOT NULL,
    sigla VARCHAR(15) NULL,
    CONSTRAINT pk_projeto_id PRIMARY KEY (id)
    );


CREATE TABLE IF NOT EXISTS coopana.preco_tabelado (
    id SERIAL NOT NULL,
    produto INT NOT NULL,
    unidade FLOAT NULL,
    valor FLOAT NULL,  --REVISAR ESSE ATRIBUTO
    projeto INT NOT NULL,
    licitação INT NOT NULL,
    CONSTRAINT pk_preco_tabelado_id PRIMARY KEY (id),
    CONSTRAINT fk_produto_id FOREIGN KEY (produto)
    REFERENCES coopana.produto (id),
    CONSTRAINT fk_licitacao_id FOREIGN KEY (licitação)
    REFERENCES coopana.licitação (id),
    CONSTRAINT fk_projeto_id FOREIGN KEY (projeto)
    REFERENCES coopana.projeto (id)
    );

CREATE TABLE IF NOT EXISTS coopana.reparticao_projeto (
    id SERIAL NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    cooperado INT NOT NULL,
    disponivel FLOAT NULL,
    entregue FLOAT NULL,
    licitação INT NOT NULL,
    CONSTRAINT pk_reparticao_projeto_id PRIMARY KEY (id),
    CONSTRAINT fk_licitacao FOREIGN KEY (licitação)
    REFERENCES coopana.licitação (id),
    CONSTRAINT fk_cooperado FOREIGN KEY (cooperado)
    REFERENCES coopana.cooperado (id)
    );

CREATE TABLE IF NOT EXISTS coopana.relatorio_entregas (
    id SERIAL NOT NULL,
    cooperado INT NOT NULL,
    produto INT NOT NULL,
    valor_unitario FLOAT,
    quantidade INT ,
    valor_total FLOAT,
    data_entrega TIMESTAMP,
    entidade_fornecedera VARCHAR(255),
    entidade_recebedora VARCHAR(255),
    CONSTRAINT pk_relatorio_entregas_id PRIMARY KEY (id),
    CONSTRAINT fk_relatorio_produto_id FOREIGN KEY (produto)
    REFERENCES coopana.produto (id),
    CONSTRAINT fk_cooperado_id FOREIGN KEY (cooperado)
    REFERENCES coopana.cooperado (id)
    );



----------------TABELAS PARA CONTROLE DE VEICULOS--------------------

CREATE TABLE IF NOT EXISTS coopana.veiculos (
    id SERIAL NOT NULL,
    tipo VARCHAR(150) NOT NULL,
    nome VARCHAR(100) NOT NULL,
    placa VARCHAR(40) NOT NULL,
    marca VARCHAR(60),
    situação VARCHAR(255),
    ano INT,
    valor FLOAT,
    CONSTRAINT pk_veiculos_id PRIMARY KEY (id));



CREATE TABLE IF NOT EXISTS coopana.funcionarios (
    id SERIAL NOT NULL,
    nome VARCHAR(255) NOT NULL,
    cpf VARCHAR(14) NOT NULL,
    telefone VARCHAR(45) NOT NULL,
    sexo VARCHAR(15),
    cargo VARCHAR(60),
    CONSTRAINT pk_funcionarios_id PRIMARY KEY (id)
    );

CREATE TABLE IF NOT EXISTS coopana.transporte (
    id SERIAL NOT NULL,
    veiculo INT NOT NULL,
    funcionario INT NOT NULL,
    destino VARCHAR(255) NOT NULL,
    saida timestamp NOT NULL,
    retorno timestamp NOT NULL,
    CONSTRAINT pk_transporte_id PRIMARY KEY (id),
    CONSTRAINT fk_funcionario_id FOREIGN KEY (funcionario)
    REFERENCES coopana.funcionarios (id),
    CONSTRAINT fk_veiculo_id FOREIGN KEY (veiculo)
    REFERENCES coopana.veiculos (id)
    );





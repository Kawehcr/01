CREATE TABLE vitins(
  id INT NOT NULL AUTO_INCREMENT,
  tutor_cod	VARCHAR(30) NOT NULL,
  DATAINTERDICAO	DATE,
  DATAMANDADO	DATE,
  DATASENTENCA	DATE,
  DATANASCIMENTOINTERDITADO	DATE,
  NUMPROCESSO	VARCHAR(60),
  NOMEJUIZMANDADO	VARCHAR(200),
  NOMEJUIZSENTANCA	VARCHAR(200),
  NOMEINTERDITADO	VARCHAR(100),
  NACIONALIDADEINTERDITADO	VARCHAR(50),
  NOMEPAIINTERDITADO	VARCHAR(100),
  NOMEMAEINTERDITADO	VARCHAR(100),
  ENDERECOINTERDITADO	VARCHAR(100),
  BAIRROITERDITADO	VARCHAR(40),
  CIDADEINTERDITADO	VARCHAR(30),
  CARTORIOCERTIDAONASCIMENTO	VARCHAR(150),
  LIVROCERTIDAONASCIMENTO	VARCHAR(30),
  FOLHACERTIDAONASCIMENTO	VARCHAR(30),
  TERMOCERTIDAONASCIMENTO	VARCHAR(30),
  LIVRO	VARCHAR(20),
  FOLHA	VARCHAR(20),
  TERMO	VARCHAR(20),
  OBSERVACAO	BLOB SUB_TYPE TEXT SEGMENT SIZE 80,
  MATRICULA	VARCHAR(50),
  CPFINTERDITADO	VARCHAR(50),
CONSTRAINT pk_vitins PRIMARY KEY (id)
);
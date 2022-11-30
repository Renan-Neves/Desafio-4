CREATE DATABASE usuario;
USE usuario;
CREATE TABLE usuario(
	id_usuario int PRIMARY KEY AUTO_INCREMENT,
	email_users varchar(50),
    assunto_users varchar(50),
    descricao_users varchar(50));
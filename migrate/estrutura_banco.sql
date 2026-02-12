CREATE DATABASE IF  NOT EXISTS onnemusic;
USE onnemusic;

CREATE TABLE IF NOT EXISTS genero (
 genero VARCHAR(30) NOT NULL PRIMARY KEY,
 icone VARCHAR(100),
 cor VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS musica (
 codigo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
 cantor VARCHAR(50),
 duracao TIME,
 nome VARCHAR(50) NOT NULL,
 url_capa VARCHAR(255),
 genero VARCHAR(30),
 CONSTRAINT fk_musica_genero FOREIGN KEY (genero) REFERENCES genero (genero)
);







CREATE DATABASE IF NOT EXISTS tmdb_movie_analysis;
USE tmdb_movie_analysis;

CREATE TABLE IF NOT EXISTS generos (
    id_genero VARCHAR(15) PRIMARY KEY,
    nome_genero VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS filmes (
    id_filme VARCHAR(15) PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    revenue BIGINT
);

CREATE TABLE IF NOT EXISTS filme_genero (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_filme VARCHAR(15),
    id_genero VARCHAR(15),
    FOREIGN KEY (id_genero) REFERENCES generos(id_genero),
    FOREIGN KEY (id_filme) REFERENCES filmes(id_filme)
);

CREATE TABLE IF NOT EXISTS elenco (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_filme VARCHAR(15),
    nome VARCHAR(255) NOT NULL,
    departamento VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_filme) REFERENCES filmes(id_filme)
);
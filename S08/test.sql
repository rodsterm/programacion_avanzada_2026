CREATE TABLE Videojuegos (
    ID INT PRIMARY KEY,
    Titulo VARCHAR(100),
    Genero VARCHAR(50),
    Clasificacion VARCHAR(20),
    Plataforma VARCHAR(50)
);

INSERT INTO Videojuegos (ID, Titulo, Genero, Clasificacion, Plataforma) VALUES
(1, 'The Legend of Zelda: Breath of the Wild', 'Aventura', 'E10+', 'Nintendo Switch'),
(2, 'FIFA 22', 'Deportes', 'E', 'Multiplataforma'),
(3, 'Cyberpunk 2077', 'RPG', 'Mature', 'PC');

SELECT * FROM Videojuegos;


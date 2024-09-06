-- Eliminar la base de datos si ya existe
DROP DATABASE IF EXISTS GestionTareas;

-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS GestionTareas;
USE GestionTareas;

-- Crear tabla de Tareas
CREATE TABLE Tarea (
    idTarea INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    tiempo_estimado FLOAT
);

-- Crear tabla de Subtareas
CREATE TABLE Subtarea (
    idSubtarea INT AUTO_INCREMENT PRIMARY KEY,
    idTarea INT,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    tiempo_estimado FLOAT,
    FOREIGN KEY (idTarea) REFERENCES Tarea(idTarea) ON DELETE CASCADE
);

-- Crear tabla de Agenda
CREATE TABLE Agenda (
    idAgenda INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    descripcion TEXT
);

-- Crear tabla de AgendaTarea
CREATE TABLE AgendaTarea (
    idAgendaTarea INT AUTO_INCREMENT PRIMARY KEY,
    idAgenda INT,
    idTarea INT,
    horaInicio TIME,
    horaFin TIME,
    completada BOOLEAN,
    tiempo_total INT,
    tiempo_dedicado INT,
    tiempo_muerto INT,
    FOREIGN KEY (idAgenda) REFERENCES Agenda(idAgenda) ON DELETE CASCADE,
    FOREIGN KEY (idTarea) REFERENCES Tarea(idTarea) ON DELETE CASCADE
);

-- Crear tabla de Eventos
CREATE TABLE Evento (
    idEvento INT AUTO_INCREMENT PRIMARY KEY,
    idAgenda INT,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    horaInicio TIME,
    horaFin TIME,
    FOREIGN KEY (idAgenda) REFERENCES Agenda(idAgenda) ON DELETE CASCADE
);

-- Crear tabla de Recordatorios
CREATE TABLE Recordatorio (
    idRecordatorio INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    idTarea INT,
    FOREIGN KEY (idTarea) REFERENCES Tarea(idTarea) ON DELETE CASCADE
);

-- Ejemplo de inserciones en la tabla de Tareas
INSERT INTO Tarea (nombre, descripcion, tiempo_estimado) VALUES
    ("Inglés", "Estudio de inglés", 1.5),
    ("Matemáticas", "Estudio de matemáticas", 2),
    ("Trabajo", "Mejoras en el trabajo y metas", 8),
    ("Meditación", "Mejorar meditación y realizarla permite muchas mejoras a nivel salud y reducción de estrés", 0.1),
    ("Sueño", "Cómo duermo", 8),
    ("Dientes", "Lavarme los dientes", 0.2),
    ("Físico", "Mejorar fuerza física", 2.0),
    ("Artes Marciales", "Mejorar técnicas marciales", 1.5),
    ("Pronunciación", "Mejorar pronunciación del mismo", 0.5),
    ("Proyectos", "Realización de tareas para mis proyectos", 1.0);

-- Ejemplo de selección de todas las tareas
SELECT * FROM Tarea;
use GestionTareas;
CREATE TABLE coches (
    id INT AUTO_INCREMENT PRIMARY KEY,
    año INT NOT NULL,
    combustible VARCHAR(50) NOT NULL,
    kilometros INT NOT NULL,
    motor VARCHAR(50) NOT NULL,
    color VARCHAR(30) NOT NULL,
    consumo DECIMAL(5,2) NOT NULL,
    cambio VARCHAR(20) NOT NULL,
    puertas INT NOT NULL,
    plazas INT NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    fecha_agregado TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE fotos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    coche_id INT NOT NULL,
    ruta VARCHAR(255) NOT NULL,
    FOREIGN KEY (coche_id) REFERENCES coches(id) ON DELETE CASCADE
);

CREATE TABLE admin (  
    id INT AUTO_INCREMENT PRIMARY KEY,  
    nombre VARCHAR(100) NOT NULL,  
    email VARCHAR(100) NOT NULL UNIQUE,  
    contraseña VARCHAR(255) NOT NULL,  
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
    es_super_admin BOOLEAN DEFAULT FALSE  
);  

CREATE TABLE mensajes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    motivo VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS registros (
    cod_localidad INTEGER,
    id_provincia INTEGER,
    id_departamento INTEGER,
    categoria VARCHAR(255), 
    provincia VARCHAR(255),
    localidad VARCHAR(255),
    nombre VARCHAR(255),
    domicilio VARCHAR(255),
    codigo_postal VARCHAR(255),
    telefono VARCHAR(255), 
    mail VARCHAR(255),
    web VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS totales_categoria (
    categoria VARCHAR(255) NOT NULL,
    total INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS totales_fuente (
    fuente VARCHAR(255) NOT NULL,
    total INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS totales_provincia (
    provincia VARCHAR(255) NOT NULL,
    categoria VARCHAR(255) NOT NULL,
    total INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS cines (
    provincia VARCHAR(255) NOT NULL,
    cant_pantallas INTEGER NOT NULL, 
    cant_butacas INTEGER NOT NULL,
    espacios_incaa INTEGER NOT NULL
);
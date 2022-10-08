CREATE TABLE IF NOT EXISTS registros (
    cod_localidad INTEGER NOT NULL,
    id_provincia INTEGER NOT NULL,
    id_departamento INTEGER NOT NULL,
    categoria VARCHAR(255) NOT NULL, 
    provincia VARCHAR(255) NOT NULL,
    localidad VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    domicilio VARCHAR(255) NOT NULL,
    codigo_postal VARCHAR(255) NOT NULL,
    telefono VARCHAR(255) NOT NULL, 
    mail VARCHAR(255) NOT NULL,
    web VARCHAR(255) NOT NULL
);


CREATE TABLE IF NOT EXISTS totales_categoria (
    categoría VARCHAR(255) NOT NULL,
    total INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS totales_fuente (
    fuente VARCHAR(255) NOT NULL,
    total INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS totales_provincia (
    provincia VARCHAR(255) NOT NULL,
    total INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS cines (
    provincia VARCHAR(255) NOT NULL,
    cant_pantallas INTEGER NOT NULL, 
    cant_butacas INTEGER NOT NULL,
    cant_espacios_INCAA INTEGER NOT NULL
);
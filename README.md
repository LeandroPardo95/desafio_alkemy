# Challenge Data Analytics + Python - Alkemy Campus

El proyecto consume datos desde 3 fuentes distintas para popular una base de datos SQL con información cultural
sobre bibliotecas, museos y salas de cines argentinos.

**Instalación:**

Ejecutar en Git Bash el siguiento comando:

`git clone https://github.com/leo9952011/desafio_alkemy`

Luego se deben instalar las librerias necesarias para correrlo, esto se hace con el siguiente comando:

`pip install -r requirements.txt`

Una vez realiazados estos pasos, ingresarar en el archivo **settings.ini** y cambiar los siguientes datos por los de su base de datos:

`USER = postgres`

`PASS = hola123`

`HOST = localhost`

`PORT = 5432`

`DB_NAME = alkemy`

**Nota:** La base de datos debe ser postgresql.

**Ejecución**

- Ejecutar el archivo "script.py" para crear las tablas dentro de la base de datos.
`python script.py`
- Ejecutar el archivo "main.py" para realizar la descarga de datos, y que los mismos sean normalizados y subidos a sus respectivas tablas dentro de nuestra base de datos.
`python main.py`



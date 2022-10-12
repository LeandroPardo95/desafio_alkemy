from pathlib import Path
from decouple import config

# DATABASE CONFIG.
USER = config("USER")
PASS = config("PASS")
HOST = config("HOST")
PORT = int(config("PORT"))
DB_NAME = config("DB_NAME")


# URLS CONFIG.
MUSEOS_URL = config("MUSEOS_URL")
CINES_URL = config("CINES_URL")
BIBLIOTECAS_URL = config("BIBLIOTECAS_URL")

# FILES CONFIG.
BASE_FILE_DIR = Path("data")

# Para transformar los meses en texto.
months = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre",
}

file_name = "{name}/{year}-{month_v}/{name}-{year}-{month}-{day}.csv"

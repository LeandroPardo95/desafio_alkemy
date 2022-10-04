from pathlib import Path
from decouple import config

# DATABASE CONFIG
USER = config('USER')
PASS = config('PASS')
HOST = config('HOST')
PORT = int(config('PORT'))
DB_NAME = config('DB_NAME')


# URLS CONFIG
MUSEOS_URL = config('MUSEOS_URL')
CINES_URL = config('CINES_URL')
BIBLIOTECAS_URL = config('BIBLIOTECAS_URL')

# DATA LIST
data = [
    {
        "name": "Museos",
        "url": MUSEOS_URL
    },
    {
        "name": "Cines",
        "url": CINES_URL,
    },
    {
        "name": "Bibliotecas",
        "url": BIBLIOTECAS_URL
    },
]

# FILES CONFIG
BASE_FILE_DIR = Path("data")

months = (
    'Enero',
    'Febrero',
    'Marzo',
    'Abril',
    'Mayo',
    'Junio',
    'Julio',
    'Agosto',
    'Septiembre',
    'Octubre',
    'Noviembre',
    'Diciembre',
)

file_name = "{name}/{year}-{month_v}/{name}-{year}-{month}-{day}.csv"

from pathlib import Path
from sqlalchemy import create_engine
from config import HOST, PORT, USER, PASS, DB_NAME


# Ubicacion del script sql que se encarga de crear las tablas
script_path = Path("sql/script.sql")

query = open(script_path).read()

engine = create_engine(f"postgresql+psycopg2://{USER}:{PASS}@{HOST}:{PORT}/{DB_NAME}")

with engine.connect() as conn:
    conn.execute(query)

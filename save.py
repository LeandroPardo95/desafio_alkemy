import pandas as pd
from script import engine


def save_data(data: list):
    """ La funcion se encarga de cargar en dataframes los archivos descargados y subirlos a la base de datos.

    Args:
        data (list): Recibe como parametro una lista con diccionarios dentro con las claves: category, y file_path, la cual nos indica la ubicación del mismo.
    """

    for file in data:
        df = pd.read_csv(file['file_path'], encoding="ISO-8859-1")

        # primero hay que normalizar los datos.

        # df.to_sql('registros', con=engine)

import pandas as pd
import logging
from config import BIBLIOTECAS_URL, CINES_URL, MUSEOS_URL
from download import Downloader
from normalizers import DataNormalizer, CineDataNormalizer, FuenteNormalizer
from loadesrs import Loader

logging.basicConfig(filename="log.log")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def run():
    # Creacion de los objetos para descargar los archivos fuente
    logger.info("Donwloading data...")
    museos = Downloader(
        "Museos",
        MUSEOS_URL,
    )
    bibliotecas = Downloader(
        "Bibliotecas",
        BIBLIOTECAS_URL,
    )
    cines = Downloader(
        "Cines",
        CINES_URL,
    )

    data_list = [museos, bibliotecas, cines]

    # Ejecutamos el metodo para descargar los archivos
    for donwloader in data_list:
        donwloader.donwload_data()
    logger.info("Donwload finished.")

    # Normalizamos los datos para la tabla registros
    logger.info("transforming data...")
    df_list = list()
    for data in data_list:
        normalizer = DataNormalizer(data.fuente, data.file_path)
        df_list.append(normalizer.transform())

    registros_df = pd.concat(df_list)

    # Normalizamos los datos para la tabla totales_categoria
    categorias_df = registros_df.groupby("categoria").size().reset_index(name="total")

    # Normalizamos los datos para la tabla totales_fuente
    totales_fuente_df = FuenteNormalizer(data_list).transform()

    # Normalizamos los datos para la tabla totales_provincia
    totales_provincia = (
        registros_df.groupby(["provincia", "categoria"])
        .size()
        .reset_index(name="total")
    )

    # Normalizamos los datos para la tabla cines
    cines_df = CineDataNormalizer(cines.fuente, cines.file_path).get_salas()

    logger.info("finished transformation.")

    # Comienza la carga de archivos en la base de datos
    logger.info("Loading data...")
    data_load = [
        {"table": "registros", "df": registros_df},
        {"table": "totales_categoria", "df": categorias_df},
        {"table": "totales_fuente", "df": totales_fuente_df},
        {"table": "totales_provincia", "df": totales_provincia},
        {"table": "cines", "df": cines_df},
    ]

    for reg in data_load:
        load = Loader(reg["table"], reg["df"])
        load.load_data()

    logger.info("Data upload finished")


if __name__ == "__main__":

    run()

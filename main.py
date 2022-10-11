from unicodedata import category
import pandas as pd
from pathlib import Path
import os

from script import engine

from config import data
from download import download_data
from normalizers import DataNormalizer, CineDataNormalizer, FuenteNormalizer
from loadesrs import Loader

if __name__ == "__main__":

    files_dir = download_data(data)

    df_list = []

    for data in files_dir:
        normalizer = DataNormalizer(data['category'], data['file_path'])

        df_list.append(normalizer.transform())

    registros_df = pd.concat(df_list)
    categorias_df = registros_df.groupby(
        'categoria').size().reset_index(name='total')
    fuentes_df = FuenteNormalizer(files_dir).transform()

    Loader('registros', registros_df).load_data()

    Loader('totales_categoria', registros_df.groupby(
        'categoria').size().reset_index(name='total')).load_data()

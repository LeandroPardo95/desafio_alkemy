import pandas as pd
from script import engine

from config import data
from download import download_data
from normalizers import DataNormalizer, CineDataNormalizer
from loadesrs import Loader

if __name__ == "__main__":

    files_dir = download_data(data)

    df_list = []

    for data in files_dir:
        normalizer = DataNormalizer(data['category'], data['file_path'])

        df_list.append(normalizer.transform())

    # concatenar y cargar
    registros_df = pd.concat(df_list)

    Loader('registros', registros_df).load_data()

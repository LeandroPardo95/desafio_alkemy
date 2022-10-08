from config import data
from download import download_data
from normalizers import DataNormalizer, CineDataNormalizer

if __name__ == "__main__":

    files_dir = download_data(data)

    df_list = []

    for data in files_dir:
        normalizer = DataNormalizer(data['category'], data['file_path'])

        df_list.append(normalizer.transform())

    # concatenar y cargar
    df_list

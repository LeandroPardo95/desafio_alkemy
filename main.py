from download import download_data
from save import save_data
from config import data

if __name__ == "__main__":

    files_dir = download_data(data)

    save_data(files_dir)

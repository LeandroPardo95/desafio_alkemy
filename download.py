import requests
from datetime import datetime
from config import BASE_FILE_DIR
from config import file_name, months


format_link = 'https://docs.google.com/spreadsheet/ccc?key={id}&output=csv'


def download_data(data: list):
    """La funcion se encarga de descargar los datos de sheets en formato csv y guardarlos en sus correspondientes rutas

    Args:
        data (list): Debe ser una lista compuesta de diccionarios que con las claves:
                    url (str): la url del archivo de google sheets.
                    name (str): nombre de la categoria.
    """
    for category in data:

        id_sheets = category["url"].split("/")[-2]
        url = format_link.format(id=id_sheets)

        file = file_name.format(
            name=category["name"],
            year=datetime.now().year,
            month=datetime.now().month,
            month_v=months[datetime.now().month - 1],
            day=datetime.now().day
        )

        m_path = BASE_FILE_DIR / file
        m_path.parent.mkdir(exist_ok=True, parents=True)

        r = requests.get(url)
        r.encoding = "utf-8"

        with open(m_path, 'w') as file:
            file.write(r.text)

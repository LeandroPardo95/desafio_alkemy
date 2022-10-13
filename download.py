from abc import ABCMeta, abstractmethod
import requests
from datetime import datetime
import logging
from config import BASE_FILE_DIR
from config import file_name, months

logger = logging.getLogger()


class AbstractDownloader(metaclass=ABCMeta):
    def __init__(self, fuente, url):
        self.fuente = fuente
        self.url = url
        self.file_path = None

    @abstractmethod
    def donwload_data(self):
        pass


class Downloader(AbstractDownloader):
    def donwload_data(self):
        """Se encarga de descargar la información de las urls y guardarlas con la siguiente ruta: "museos/2021-noviembre/museos-03-11-2021” (la fecha y categoria según corresponda).
        Una vez guardados los archivos, las rutas son almacenadas en el atributo self.file_path, con el fin de reutilizarlas en cualquier momento.
        """

        # Formato de link para descargar la hoja de sheets en formato csv
        format_link = "https://docs.google.com/spreadsheet/ccc?key={id}&output=csv"

        id_sheets = self.url.split("/")[-2]

        url = format_link.format(id=id_sheets)

        # Configuración del nombre y ruta del archivo
        file = file_name.format(
            name=self.fuente,
            year=datetime.now().year,
            month=datetime.now().month,
            month_v=months[datetime.now().month],
            day=datetime.now().day,
        )

        m_path = BASE_FILE_DIR / file
        m_path.parent.mkdir(exist_ok=True, parents=True)

        try:
            r = requests.get(url)
            r.encoding = "utf-8"

            with open(m_path, "w") as file:
                file.write(r.text)

            self.file_path = m_path.resolve()
        except:
            logger.error(f"There was an error downloading {self.fuente}")
            raise Exception(
                f"La descargar de {self.fuente} fallo. Verifique que la url sea correcta."
            )

        return super().donwload_data()

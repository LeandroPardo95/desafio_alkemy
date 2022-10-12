from abc import ABCMeta, abstractmethod
import requests
from datetime import datetime
from config import BASE_FILE_DIR
from config import file_name, months


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

        format_link = "https://docs.google.com/spreadsheet/ccc?key={id}&output=csv"

        id_sheets = self.url.split("/")[-2]

        url = format_link.format(id=id_sheets)

        file = file_name.format(
            name=self.fuente,
            year=datetime.now().year,
            month=datetime.now().month,
            month_v=months[datetime.now().month],
            day=datetime.now().day,
        )

        m_path = BASE_FILE_DIR / file
        m_path.parent.mkdir(exist_ok=True, parents=True)

        r = requests.get(url)
        r.encoding = "utf-8"

        with open(m_path, "w") as file:
            file.write(r.text)

        self.file_path = m_path.resolve()

        return super().donwload_data()

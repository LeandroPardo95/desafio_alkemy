from abc import ABCMeta, abstractmethod
from script import engine
import logging

logger = logging.getLogger()


class AbstractLoader(metaclass=ABCMeta):
    def __init__(self, table, dataframe):
        self.df = dataframe
        self.table = table

    @abstractmethod
    def load_data(self):
        pass


class Loader(AbstractLoader):
    def load_data(self):
        """El metodo se encargar de subir los pd.DataFrame a la base de datos. Para esto utiliza el engine con los datos para realizar la conexion a la BD, en metodo .to_sql de la librerias pandas y los atributos:
        self.table (str) -> Nombre de la tabla a la que se deben subir los datos.
        self.df (pd.DataFrame) -> Dataframe con la informacion ya normalizada que se desea subir.
        """

        logger.debug(f"Loading the table {self.table}")

        self.df.to_sql(self.table, con=engine, if_exists="append", index=False)

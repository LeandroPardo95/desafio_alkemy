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

        logger.debug(f"Loading the table {self.table}")

        self.df.to_sql(self.table, con=engine, if_exists="append", index=False)

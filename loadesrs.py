from abc import ABCMeta, abstractmethod
import pandas as pd
from script import engine


class AbstractLoader(metaclass=ABCMeta):
    def __init__(self, table, dataframe):
        self.df = dataframe
        self.table = table

    @abstractmethod
    def load_data(self):
        pass


class Loader(AbstractLoader):
    def load_data(self):

        self.df.to_sql(self.table, con=engine, if_exists="append", index=False)

        print("Datos subidos a la base de datos")

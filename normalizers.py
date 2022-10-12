from abc import ABCMeta, abstractmethod
from pathlib import Path
from unicodedata import name
import pandas as pd
from sqlalchemy import column


class AbstractNormalizer(metaclass=ABCMeta):
    def __init__(self, nombre, path) -> None:
        self.nombre = nombre
        self.path = path

    @abstractmethod
    def transform(self):
        pass


class DataNormalizer(AbstractNormalizer):
    def transform(self):

        df = pd.read_csv(self.path, encoding="ISO-8859-1")

        rename_columns = {
            "Cod_Loc": "cod_localidad",
            "IdProvincia": "id_provincia",
            "IdDepartamento": "id_departamento",
            "Categoría": "categoria",
            "Provincia": "provincia",
            "Localidad": "localidad",
            "Nombre": "nombre",
            "Domicilio": "domicilio",
            "direccion": "domicilio",
            "Dirección": "domicilio",
            "CP": "codigo_postal",
            "Teléfono": "telefono",
            "Mail": "mail",
            "Web": "web",
        }

        columns = [
            "cod_localidad",
            "id_provincia",
            "id_departamento",
            "categoria",
            "provincia",
            "localidad",
            "nombre",
            "domicilio",
            "codigo_postal",
            "telefono",
            "mail",
            "web",
        ]

        df.rename(columns=rename_columns, inplace=True)

        return df[columns]


class CineDataNormalizer(DataNormalizer):
    def get_salas(self) -> pd.DataFrame:
        """_summary_

        Returns:
            pd.DataFrame: _description_
        """

        df = pd.read_csv(self.path, encoding="ISO-8859-1")

        rename_columns = {
            "Provincia": "provincia",
            "Pantallas": "cant_pantallas",
            "Butacas": "cant_butacas",
            "espacio_INCAA": "espacios_incaa",
        }

        columns = [
            "cant_pantallas",
            "cant_butacas",
            "espacios_incaa",
        ]
        df.rename(columns=rename_columns, inplace=True)

        # La columna cantidad_espacios_INCAA contiene valores tipo Nan y cadenas de texto como "si" o "Si" haciendo referencia a aquellos espacios que deben ser contabilizados como un espacio INCAA, por lo tanto se deben reemplazar los Nan -> 0 y los "si" por un 1, y convertirlos a tipo numericos.
        df["espacios_incaa"] = (
            df["espacios_incaa"]
            .fillna(0)
            .astype("string")
            .str.replace("si", "1", case=False)
            .astype("int")
        )

        # Se agrupan los datos por provincias y obtenemos la suma de las columnas que necesitamos
        df_res = df.groupby("provincia").sum(numeric_only=True)[columns].reset_index()

        return df_res


class FuenteNormalizer:
    def __init__(self, data: list):
        self.data = data

    def transform(self) -> pd.DataFrame:

        fuente_list = list()

        for fuente in self.data:
            df = pd.read_csv(fuente.file_path, encoding="ISO-8859-1")

            fuente_list.append({"fuente": fuente.fuente, "total": len(df.index)})

        return pd.DataFrame(fuente_list)

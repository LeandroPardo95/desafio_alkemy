from abc import ABCMeta, abstractmethod
import pandas as pd
import logging

logger = logging.getLogger()


class AbstractNormalizer(metaclass=ABCMeta):
    def __init__(self, nombre, path) -> None:
        self.nombre = nombre
        self.path = path

    @abstractmethod
    def transform(self):
        pass


class AbstractFuenteNormalizer(metaclass=ABCMeta):
    def __init__(self, data: list) -> None:
        self.data = data

    @abstractmethod
    def transform(self):
        pass


class DataNormalizer(AbstractNormalizer):
    def transform(self) -> pd.DataFrame:
        """El metodo se encargar de normalizar los datos descargardos de las fuentes, seleccionando y renombrando las columnas que son necesarias para realizar el analisis.

        Returns:
            pd.DataFrame: Retorna un objeto de tipo pd.DataFrame que contiene las tablas indicadas en la lista columns.
        """

        logger.debug(f"transforming {self.nombre}")

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
        """El metodo se encarga de normalizar los datos de la fuente que contiene los datos de cines.

        Returns:
            pd.DataFrame: un objeto de tipo DataFrame que contiene los datos con las siguientes tablas:
                provincias -> Datos agrupados en provincia (str)
                cant_pantallas -> Suma de todas las pantallas correspondientes a la provincia (int)
                cant_butacas -> Suma de todas las butacas correspondientes a la provincia (int)
                espacios_incaa -> Suma de todas las salas que contienen un "si" en la columna espacio_INCAA (int)
        """

        logger.debug(f"transforming {self.nombre}")

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


class FuenteNormalizer(AbstractFuenteNormalizer):
    def transform(self) -> pd.DataFrame:
        """El metodo se encarga de construir un dataframe que contenga todas las fuentes y la cantidad de registros de c/u. Esto se logra a partir del contendio del atributo self.data, el mismo debe ser una lista de objetos Downloader, ya que para realizar dicha tabla se necesita trabajar con el nombre de la fuente y el file_path.

        Returns:
            pd.DataFrame: Objeto DataFrame con las columnas:
                "fuente" -> Nombre de cada fuente
                "total" -> Cantidad de registros de la misma.
        """

        logger.debug(f"transforming fuentes")

        fuente_list = list()

        for fuente in self.data:
            df = pd.read_csv(fuente.file_path, encoding="ISO-8859-1")

            fuente_list.append({"fuente": fuente.fuente, "total": len(df.index)})

        return pd.DataFrame(fuente_list)

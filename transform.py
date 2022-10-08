import pandas as pd

# ESTE ARCHIVO SE DESCARTO, LA TRANSFORMACION DE DATOS SE ESTABA HACIENDO DE ESTA MANERA PERO DECIDI CAMBIAR A CLASES, PARA MANEJAR MEJOR LOS REGISTROS DE LOS CINES.


# def transform_data(data: list) -> list:
#     """ La funcion se encarga de cargar en dataframes los archivos descargados y subirlos a la base de datos.

#     Args:
#         data (list): Recibe como parametro una lista con diccionarios dentro con las claves: category, y file_path, la cual nos indica la ubicación del mismo.


#     Returns:
#         list:
#     """

#     df_list = []

#     for file in data:
#         df = pd.read_csv(file['file_path'], encoding="ISO-8859-1")

#         df.rename(columns={
#             "Cod_Loc": "cod_localidad",
#             "IdProvincia": "id_provincia",
#             "IdDepartamento": "id_departamento",
#             "Categoría": "categoria",
#             "Provincia": "provincia",
#             "Localidad": "localidad",
#             "Dirección": "domicilio",
#             "direccion": "domicilio",
#             "Domicilio": "domicilio",
#             "Nombre": "nombre",
#             "CP": "codigo_postal",
#             "Teléfono": "telefono",
#             "Mail": "mail",
#             "Web": "web",
#         }, inplace=True)

#         column_list = [
#             "cod_localidad",
#             "id_provincia",
#             "id_departamento",
#             "categoria",
#             "provincia",
#             "localidad",
#             "nombre",
#             "domicilio",
#             "cp",
#             "telefono",
#             "mail",
#             "web",
#         ]

#         df_list.append(df[column_list])

#     dfs = pd.concat(df_list)

#     return dfs

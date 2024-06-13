# import pandas as pd
# import numpy as np

# crear un dataframe desde un diccionario

# datos = {
#     "Nombre": ["Pablo", "Eduardo", "Juan", "Laura"],
#     "Edad": [24, 59, 23, 56]
# }


# df = pd.DataFrame(datos)
# # Agrego una nueva fila al dataframe, asigno el indice y concateno
# nueva_fila = pd.DataFrame({"Nombre": "Pedro", "Edad": 18}, index=[4])

# # Si no sabemos bien cual es el index, colocamos reset.index(drop= true), eso resetea los indices
# df = pd.concat([df, nueva_fila]).reset_index(drop=True)
# print(df)

# Otra manera de crear un dataframe
# datos2 = [{'Nombre': 'Pablo', 'Edad': 24},
#           {'Nombre': 'Juan', 'Edad': 24}
#           ]
# df2 = pd.DataFrame(datos2)
# print(df2)

# utilizando numpy
# datos = np.array([[1, 2, 3], [4, 5, 6]])
# df = pd.DataFrame(datos)
# print(df)


# banco = pd.read_csv("pythonpractica\\python_practica\\archivos\\bank.csv")
# print(banco["Geography"])  # para seleccionar unicamente una columna

# # Selecciono unicamente columns enteras
# columnas_enteras = banco.select_dtypes(include='int64')
# print(columnas_enteras)
# df_vacio = pd.DataFrame()

# selecciono primeras cuatro columnas
# primeras_4 = banco.iloc[:, :4]
# print(primeras_4)

# Selecciono las columnas que empiecen con la letra "f"
# banco_f = banco.loc[:, banco.columns.str.startswith('f')]
# print(banco_f)

# para hacer un print de la primera fila
# print(banco.iloc[0])


# aplico filtro a la columna "Age"
# mayores_40 = banco[banco['Age'] > 40]
# print(mayores_40)

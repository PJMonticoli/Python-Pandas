import pandas as pd
import numpy as np

# crear un dataframe desde un diccionario

# datos = {
#     "Nombre": ["Pablo", "Eduardo", "Juan", "Laura"],
#     "Edad": [24, 59, 23, 56]
# }


# df = pd.DataFrame(datos)
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


banco = pd.read_csv("pythonpractica\\python_practica\\archivos\\bank.csv")
# print(banco["Geography"]) #para seleccionar unicamente una columna

# para seleccionar unicamente las columnas enteras
columnas_enteras = banco.select_dtypes(include='int64')
print(columnas_enteras)
df_vacio = pd.DataFrame()

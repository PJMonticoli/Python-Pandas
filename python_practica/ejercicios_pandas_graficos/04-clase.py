import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [5, np.nan, 7, 8],
                   'C': [9, 10, 11, 12]})
# print(df)  # print(df.isnull())con isnull() verificamos que si hay valores null en el df

# Eliminamos columnas axis= 0 filas axis=1 columnas
# df_drop_columns = df.dropna(axis=1)
# print(df_drop_columns)


# Llenar datos faltantes con un valor constante
df_fill = df.fillna(value=0)
print(df_fill)

# df.fillna(method='ffill') => llena datos faltantes con el valor de la fila anterior
df_fill_alternativo_ffill = df.fillna(method='ffill')
# print(df_fill_alternativo_ffill)

# llena datos faltantes con el valor de la fila siguiente
df_fill_alternativo_bfill = df.fillna(method='bfill')
# print(df_fill_alternativo_bfill)

# llena el dato faltante con el promedio de toda la columna
df_fill_alternativo_promedio = df.fillna(df.mean())
# print(df_fill_alternativo_promedio)

# llenado de datos faltantes usando la interpolacion
# llena con el valor "ideal" que deberia de ir en ese espacio
df_fill_interpolate = df.interpolate()
print(df_fill_interpolate)

import pandas as pd
import numpy as np

# Creando DataFrame numeros aleatorios entre 1-10. 3 filas 2 columnas
# df1 = pd.DataFrame(np.random.randint(1, 10, size=(3, 2)), columns=list('AB'))
# df2 = pd.DataFrame(np.random.randint(1, 10, size=(3, 2)), columns=list('AB'))
# print(df1)
# print(df2)

# Operaciones aritmeticas con escalares
# df1_plus_2 = df1 + 2
# print(df1_plus_2)


# diferencia = df1 - df2
# print(diferencia)

# Uso de funciones matematicas de NumPy. Aplico raiz cuadrada
# df_sqrt = np.sqrt(df1)
# print(df1)


# df = pd.DataFrame(np.random.randint(
#     1, 10, size=(10, 4)), columns=list('ABCD'))
# print(df)

# Uso funciones de agregacion en columnas.
# Sumo toda la columna A
# df_sum = df['A'].sum()

# Obtengo el valor min de la columna.
# df_min = df['A'].min()
# print(df_min)

# Metodo agg => Por cada una de las column calculo sum,mean,max,min
# df_agg = df.agg(['sum', 'mean', 'max', 'min'])
# print(df_agg)


# df = pd.DataFrame({
#     "A": ["Perro", "Gato", "Perro", "Gato", "Perro", "Gato"],
#     "B": ["uno", "uno", "dos", "tres", "dos", "uno"],
#     "C": np.random.rand(6),
#     "D": np.random.rand(6)
# })

# print(df)

# Agrupacion por una columna
# grouped_single = df.groupby(['A', 'B']).sum() # puedo agrupar por min,max,mean

# Uso de la funcion agg con groupby
# grouped_single = df.groupby(['A', 'B']).agg(['sum', 'mean'])
# print(grouped_single)


df1 = pd.DataFrame({
    'A': ['AD', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'key': ['K0', 'K1', 'K2', 'K3']
})

df2 = pd.DataFrame({
    'C': ['CD', 'C1', 'C2', 'C3', 'C4'],
    'D': ['D0', 'D1', 'D2', 'D3', 'D4'],
    'key': ['K0', 'K1', 'K2', 'K3', 'K4']
})
print(df1)
print(df2)
# axis=0: Concatenación vertical
# axis=1: Concatenación horizontal
# df_concat = pd.concat([df1, df2], axis=0).reset_index()

# Reemplazar NaN por "0"
# df_concat = df_concat.fillna("0")
# print(df_concat)

# on => variable con la que queremos hacer el merge
# outer => toma todos los valores de ambos dataframe y los une
df_merge_outer = pd.merge(df1, df2, on='key', how='outer')
# inner => une solamente los dataframe que tienen la misma key
df_merge_inner = pd.merge(df1, df2, on='key', how='inner')
print(df_merge_outer)
print(df_merge_inner)

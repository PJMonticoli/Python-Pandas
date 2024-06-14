import pandas as pd

data = {'Nombre': ['Pablo Monticoli', 'Eduardo Monticoli', 'Juan Oller', 'Laura Castagna'],
        'Edad': [24, 59, 24, 57],
        'Ciudad': ['Córdoba', 'Jesus Maria', 'Sevilla', 'Madrid']}

df = pd.DataFrame(data)


# Ordenar por una columna => edad, por defecto es ascending=True
# df = df.sort_values(by='Edad')
# print(df)

# # Ordenar por una columna => edad, de manera desc
# df = df.sort_values(by='Edad', ascending=False)
# print(df)

# Ordenar por multiples columnas. Primero ordena por edad, luego por ciudad
# df = df.sort_values(by=['Edad', 'Ciudad']).reset_index(drop=True)

# Ordenar por indice de fila
# df = df.sort_index()

# inplace=True modifica el DataFrame original, sin necesidad de crear una copia
# df.reset_index(drop=True, inplace=True)

# Esto en cambio devuelve una copia del dataframe con el index restablecido
# df = df.reset_index(drop=True)

# Crear un ranking basico en base a columna Edad
# df['Ranking_Edad'] = df['Edad'].rank()

# Es lo mismo que aplicar el metodo     rank(method='average')
# df['Ranking_Edad'] = df['Edad'].rank(method='average')
print(df)

# import pandas as pd

# data = {'nombre': ['Pablo Monticoli', 'Eduardo Monticoli', 'Laura Castagna'],
#         'edad': [24, 59, 57],
#         'ciudad': ['Córdoba', 'Jesus Maria', 'Madrid']}

# df = pd.DataFrame(data)
# print(df)

# Le sumo 5 años a cada fila de la column edad
# df['edad'] = df['edad'].apply(lambda x: x+5)
# print(df)

# Convierto a mayuscula cada fila de la column nombre
# def convertir_may(x):
#     return x.upper()

# df['nombre'] = df['nombre'].apply(convertir_may)
# print(df)

# imprimo el promedio edad con mean. No hace falta el apply aca.
# promedio_edad = df['edad'].mean()
# print(promedio_edad)

# reemplazando valores column nombre
# df['nombre'] = df['nombre'].replace(
#     'Pablo Monticoli', 'Pablo Javier Monticoli')

# # reemplazo valores column nombre. Armo lista de las filas a reemplazar y lista de nuevos valores
# df['nombre'] = df['nombre'].replace(
#     ['Pablo Monticoli', 'Eduardo Monticoli'],
#     ['Pablo Javier Monticoli', 'Eduardo Mario Monticoli'])
# print(df)

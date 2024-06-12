import pandas as pd

df = pd.read_csv("pythonpractica\\python_practica\\archivos\\jugadores.csv")

# print(df.head(5))  # obtengo los primeros 5 del archivo


# df_ordenado = df.sort_values('nombre')  # ordeno el df por nombre
# print(df_ordenado)

# cargo unicamente los jugadores que cumplan la condicion establecida
df_filtrado = df[df['goles'] > 100]
print(df_filtrado)

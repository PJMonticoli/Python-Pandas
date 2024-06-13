import pandas as pd

# cargo archivo csv con seleccion de columns
# df = pd.read_csv("pythonpractica\\python_practica\\archivos\\bank.csv", usecols=[
#                  'Surname', 'Geography', 'Gender', 'Age', 'EstimatedSalary'])
# print(df)


# pip install lxml html5lib para cargar datos HTML desde un sitio web

# Leer la tabla de fútbol desde el sitio web
tablas_futbol = pd.read_html(
    'https://www.tycsports.com/estadisticas/premier-league-de-inglaterra/tabla-de-posiciones.html')[0]  # Asumir que la tabla de interés es la primera tabla_futbol = tablas_futbol[0]

# Imprimir el DataFrame
print(tablas_futbol)
# Exportar el DataFrame a CSV. El sep ; es para que separe bien las columnas.
# Entre [] especifico cuales columnas son las que quiero guardar
# para solucionar el tema de tildes y caracteres especiales utilizo encoding='utf-8-sig'
tablas_futbol[['Pos', 'Equipo', 'Pts']].to_csv(
    'pythonpractica\\python_practica\\archivos\\tabla_posiciones.csv', index=False, sep=';')

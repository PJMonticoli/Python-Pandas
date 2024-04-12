import re

texto = '''Hola maestro,esta es la cadena numero 1. Todo bien?
 Esta es la  linea 12345 de texto.
 Esta es la cadena FINAL (linea 3) maestro'''

# Haciendo una busqueda simple
# resultado = re.findall("Esta",texto) # flags=re.IGNORECASE con el re.IGNORECASE ignoro las mayusculas/minusculas

# \d  => busqueda digitos numericos del 0-9
# resultado = re.findall(r"\d",texto)

# \D  => busqueda TODO MENOS digitos numericos del 0-9
# resultado = re.findall(r"\D",texto)

#\w => busca caracteres alfanumericos [a-z] [A-Z] [0-9 _] => _ se considera alfanumerico
# resultado = re.findall(r"\w",texto)

#\W => busca TODO MENOS caracteres alfanumericos [a-z] [A-Z] [0-9 _] => _ se considera alfanumerico
# resultado = re.findall(r"\W",texto)

#\s => busca espacios en blanco  => espacios,tabs,saltos de linea 
# resultado = re.findall(r"\s",texto)

#\S => busca TODO MENOS espacios en blanco  => espacios,tabs,saltos de linea 
# resultado = re.findall(r"\S",texto)

# . busca TODO MENOS saltos de linea
# resultado = re.findall(r".",texto)

# \n busca  saltos de linea
# resultado = re.findall(r"\n ",texto)
# \. busca los puntos => con \. cancelo la funcionalidad que tiene por defecto el .
# resultado = re.findall(r"\.",texto) 

# armando una cadena que busque un numero,seguido de un punto y espacio
# resultado = re.findall(f"\d\.\s",texto)

# ^ => busca el comienzo de una linea, ejemplo busco Hola al principio de la linea. Devuelve resultado si encuentra y sino []
# resultado = re.findall(f"^Hola",texto) # si agrego el parametro flags=re.M  para que sea multinea,es decir, que interprete cada linea como una nueva.

# $ busca el final de una linea
# resultado = re.findall(f"maestro$",texto,flags=re.M)

# {n} busca n cantidad de veces el valor de la izquierda, en este caso encuentra en el texto una parte que haya 3 digitos numericos juntos
# resultado = re.findall(r"\d{3}",texto)

# {n,m} al menos n, como maximo m 
resultado = re.findall(r"\d{1,4}",texto)
print(resultado)    
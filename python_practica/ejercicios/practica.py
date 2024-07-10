"""
EL FAMOSO "FIZZ BUZZ"
Escribe un programa que muestre por 
consola (con un print) los números 
de 1 a 100 (ambos incluidos y con 
un salto de línea entre cada 
impresión), sustituyendo 
los siguientes:

Múltiplos de 3 por la palabra "fizz".
Múltiplos de 5 por la palabra "buzz".
Múltiplos de 3 y de 5 a la vez por
la palabra "fizzbuzz".
"""

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("fizzbuzz")
#     elif number % 3 == 0:
#         print("fizz")
#     elif number % 5 == 0:
#         print("buzz")
#     else:
#         print(number)


"""
DECIMAL A BINARIO
Crea un programa se encargue de
transformar un número decimal a binario.
"""


# def decimal_to_binary(decimal):

#     binary = ""

#     while decimal > 0:
#         binary = f"{decimal% 2}{binary}"
#         decimal //= 2

#     return "0" if binary == "" else binary


# print(decimal_to_binary(10))


"""
PAR O IMPAR
Crea un programa que compruebe si
un número entero es par o impar.
"""

# try:
#     number = int(input("Ingrese un número "))
#     if number % 2 == 0:
#         print(f"El numero {number} es PAR")
#     else:
#         print(f"El número {number} es IMPAR")

# except ValueError:
#     print("Número no valido")


"""
CONTADOR DE VOCALES
Crea un programa que cuente cuantas
vocales tiene una cadena de texto.
"""


# vocales = "aeiou"
# contador = 0
# text = str(input("Ingrese una palabra "))
# for caracter in text.lower():
#     if caracter in vocales:
#         contador += 1
# print(f"Total vocales: {contador}")


"""
IMC
Crea una calculadora del
índice de masa corporal.
"""

# weight = float(input("Ingrese el Peso en kg: "))
# height = float(input("Ingrese la Altura en m: "))

# imc = weight / (height ** 2)

# print(f"El IMC es de : {imc:.2f}") # número de punto flotante (decimal) con 2 decimales.

# if imc < 18.5:
#     print("Peso bajo")
# elif 18.5 <= imc < 24.9:
#     print("Peso normal")
# elif 25 <= imc < 29.9:
#     print("Sobrepeso")
# else:
#     print("Obesidad")


"""
CONVERSOR DE TEMPERATURAS
Crea un conversor entre
grados Celsius y Fahrenheit. 
"""

# print("Conversor de Temperaturas:")
# print("1. Celsius a Fahrenheit")
# print("2. Fahrenheit a Celsius")

# choice = input("Elige una opción: ")

# degrees = float(input("Temperatura: "))

# if choice == "1":
#     fahrenheit = (degrees * 9/5) + 32
#     print(f"{degrees}°C son {fahrenheit}°F.")
# elif choice == "2":
#     celsius = (degrees - 32) * 5/9
#     print(f"{degrees}°F son {celsius}°C.")
# else:
#     print("Opción no válida.")


"""
ANAGRAMAS
Comprueba si dos cadenas
de texto son anagramas.
"""

# def are_anagrams(string1, string2):
#     return sorted(string1.lower()) == sorted(string2.lower())

# print(are_anagrams("Roma", "Amor"))
# print(are_anagrams("Amiga", "Magia"))
# print(are_anagrams("Hola", "Pablo"))


"""
TABLAS DE MULTIPLICAR
Imprime todas las tablas de
multiplicar de 1 al 10.
"""

# for table_number in range(1, 11):
#     print(f"Tabla del {table_number}")
#     for number in range(1, 11):
#         print(f"{number} x {table_number} = {number * table_number}")
#         print()


"""
INVERSIÓN DE CADENAS
Crea una función que invierta
una cadena de texto.
"""


# def reverse_string(text):
#     reversed_string = ""
#     for char in text:
#         reversed_string = char + reversed_string
#     return reversed_string


# print(reverse_string("Hola, mundo!"))

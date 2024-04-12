## Falta el profesor y se decide que la clase la va a dar el alumno de mayor edad y el asistente sera el de menor edad

# def obtener_compañeros(cantidad_de_compañeros):
#     compañeros = []
#     for i in range(cantidad_de_compañeros):
#         nombre = input("Ingrese el nombre del compañero: ")
#         edad = input("Ingrese la edad: ")
#         compañero = (nombre,edad)
#         compañeros.append(compañero)
#     compañeros.sort(key=lambda x:x[1])
#     asistente = compañeros[0][0]
#     profesor = compañeros[-1][0]
#     return asistente,profesor

# asistente,profesor = obtener_compañeros(5)
# print(f"El asistente es {asistente} y el profesor {profesor}")


## creo una funcion que me devuelva los numeros primos entre 0 y el argumento que pasamos
# def es_primo(num):
#     for i in range(2,num-1):
#         if num%i==0: return False
#     return True

# def primos_hasta(num):
#     primos =[]
#     for i in range(3,num+1):
#         resultado = es_primo(i)
#         if resultado == True : primos.append(i)
#     return primos


# resultado = primos_hasta(13)
# print(resultado)


## creo una funcion que muestre la serie de fibonacci entre 0 y el numero dado
# def fibonacci(num):
#     a,b = 0,1 ## aca creo una tupla => la puedo crear con o sin parentesis
#     lista_fibonacci = [0]
#     for i in range(num):
#         if b > num: return lista_fibonacci
#         else: 
#             lista_fibonacci.append(b)
#             a,b = b,a+b ## aca desempaqueto    a = b y b = a +b
# resultado = fibonacci(20)
# print(resultado)
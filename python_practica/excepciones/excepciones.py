# #creo funcion que suma numeros
# def sumar_dos():
#     #inicio bucle
#     while True:
#         #pido numeros
#         a = input("Número 1: ")
#         b = input("Número 2: ")
#         try:
#             # convierto a enteros
#             resultado = int(a) + int(b)
#             #creo excepcion para evitar que el programa se detenga
#         except Exception as e: 
#             print(f"Ingrese valores numericos, error :{e}")    
#         else:
#             break
#         finally:
#             print("Manejo de excepcion finalizado")
#     return resultado

# print(sumar_dos())
# /*
#  * EJERCICIO:
#  * Explora el concepto de callback en tu lenguaje creando un ejemplo
#  * simple (a tu elección) que muestre su funcionamiento.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un simulador de pedidos de un restaurante utilizando callbacks.
#  * Estará formado por una función que procesa pedidos.
#  * Debe aceptar el nombre del plato, una callback de confirmación, una
#  * de listo y otra de entrega.
#  * - Debe imprimir un confirmación cuando empiece el procesamiento.
#  * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
#  *   procesos.
#  * - Debe invocar a cada callback siguiendo un orden de procesado.
#  * - Deb


import random
import time
import threading

def proceso_saludo(nombre : str,callback):
    print("Ejecutando proceso de saludo...")
    callback(nombre)
    
def respuesta_saludo(nombre : str):
    print(f"Hola {nombre}, Bienvenido!")


proceso_saludo("Pablo", respuesta_saludo)


def orden_proceso(plato : str, confirm_callback,ready_callback,delivered_callback):
    def proceso():
        confirm_callback(plato)
        time.sleep(random.randint(1, 10))
        ready_callback(plato)
        time.sleep(random.randint(1,10))
        delivered_callback(plato)
        time.sleep(random.randint(1,10))
        
    threading.Thread(target=proceso).start()
    
def confirm_callback(plato : str):
    print(f"Tu pedido {plato} a sido confirmado..")
    
def ready_callback(plato : str):
    print(f"Tu pedido {plato} esta listo..")
    
def delivered_callback(plato : str):
    print(f"Tu pedido {plato} ha sido entregado..")


orden_proceso("Hamburguesa triple", confirm_callback,ready_callback,delivered_callback)
orden_proceso("Pizaa de palmito", confirm_callback,ready_callback,delivered_callback)
orden_proceso("Pizaa especial", confirm_callback,ready_callback,delivered_callback)
# Aca en Python puedo hacer polimorfismo de herencia sin necesidad de heredar el metodo de otra clase
# ya que es un lenguaje de tipado dinamico
class Gato():
    def sonido(self):
        print("Miau")

class Perro():
    def sonido(self):
        print("Guau")

def hacer_sonido(animal):
    print(animal.sonido())        
gato = Gato()
perro = Perro()
hacer_sonido(gato)
# gato.sonido()
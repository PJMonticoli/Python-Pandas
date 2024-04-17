# class Persona():
#     def __init__(self,nombre,edad):
#         self.nombre = nombre
#         self.edad= edad
    
#     def mostrar_datos(self):    
#         print(f"Nombre: {self.nombre}")
#         print(f"Edad: {self.edad}")

# class Estudiante(Persona):
#     def __init__(self,nombre,edad,grado):
#         super().__init__(nombre,edad)
#         self.grado = grado
#     def mostrar_grado(self):
#         print(f"Nombre: {self.grado}")

# estudiante = Estudiante("Pablo",24,"Universidad")
# estudiante.mostrar_datos()
# estudiante.mostrar_grado()

class Animal():
    def comer(self):
        print("El animal esta comiendo")

class Mamifero(Animal):
    def amamantar(self):
        print("El animal esta amamantando")
class Ave(Animal):
    def volar(self):
        print("El animal esta volando")
class Murcielago(Mamifero,Ave):
    pass

murcielago = Murcielago()
murcielago.amamantar()
murcielago.volar()
murcielago.comer()

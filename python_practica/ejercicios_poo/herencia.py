class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
# class Empleado(Persona): 
#     #pass # => con esto creo la clase y de momento la dejo sin hacer nada
#     def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
#         super().__init__(nombre,edad,nacionalidad)
#         self.trabajo = trabajo
#         self.salario = salario
# class Estudiante(Persona):
#     def __init__(self,nombre,edad,nacionalidad,notas,universidad):
#         super().__init__(nombre,edad,nacionalidad)
#         self.notas = notas
#         self.universidad = universidad

class Artista():
    def __init__(self,habilidad):
        self.habilidad =habilidad
    def mostrar_habilidad(self):
        return(f"Mi habilidad es: {self.habilidad}")

class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
    
    def presentarse(self):
        print(f"Hola, soy {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}") 

pablo  = EmpleadoArtista("Pablo",24,"Argentina","Futbol",100000,"Guma")
pablo.presentarse()
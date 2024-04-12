# class Estudiante:
#     def __init__(self,nombre,edad,grado):
#         self.nombre = nombre
#         self.edad = edad
#         self.grado = grado
#     def estudiar(self):
#         print(f"El estudiante esta estudiando: {self.grado}")
    
# estudiante1 = Estudiante("Pablo","24","Programación")

# estudiante1.estudiar()


class Estudiante:
    def __init__(self,nombre,edad,curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
    def estudiar(self):
        print("Estudiando...")
    
nombre = input("Ingrese el nombre del estudiante: ")
edad = input("Ingresela edad del estudiante: ")
grado = input("Ingrese el curso del estudiante: ")

estudiante = Estudiante(nombre,edad,grado)

print(f""" 
      DATOS DEL ESTUDIANTE \n
        NOMBRE: {estudiante.nombre} \n
        EDAD {estudiante.edad} años \n
        CURSO {estudiante.curso}
""")


estudiante.estudiar()
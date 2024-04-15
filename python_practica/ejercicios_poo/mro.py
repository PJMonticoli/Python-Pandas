class A:
    def hablar(self):
        print("Hola desde clase A")
class B(A):
    def hablar(self):
        print("Hola desde clase B")

class C(A):
    def hablar(self):
        print("Hola desde clase C")


class D(B,C):  #=> aca le digo el orden de prioridad es b y luego c,si no encuentra nada va la clase A.
    def hablar(self):
        print("Hola desde clase D")

d= D()
d.hablar()
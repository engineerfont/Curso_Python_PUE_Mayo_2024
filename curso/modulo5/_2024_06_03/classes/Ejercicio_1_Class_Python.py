# Definir una clase con los siguientes atributos:
# Variables de instancia:
# - nombre
# - edad
# - altura
# Métodos de la clase:
# - init(), en el cual creamos las variables de instancia
# - mostrar(), mostrará los valores de todas las variables de instancia

class Persona():

    def init(self):
        self.nombre = 'Ana'
        self.edad = 32
        self.altura = 1.78

    def mostrar(self):
        print(self.nombre)
        print(self.edad)
        print(self.altura)


persona = Persona()
#persona.init()
persona.mostrar()


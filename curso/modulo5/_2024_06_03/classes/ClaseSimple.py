class Simple(object):
    pass

class ClasePython(object):

    def __init__(self): # El constructor de la clase
        pass

    def __str__(self): # Este método es equivalente al toString()
        pass

    def __eq__(self, other):
        pass



    NOMBRE = 'Xoan' # Variable de clase

    # Definir variables de clase

    # Definir métodos

    def mostrar(self):
        self.Edad = 28

    def show(self):
        self.Edad += 2


    # Variables de instancia de clase, que se definen dentro
    # de los métodos


print(ClasePython.NOMBRE)

persona = ClasePython()

#print(persona.Edad)

persona.mostrar()

print(persona.Edad)



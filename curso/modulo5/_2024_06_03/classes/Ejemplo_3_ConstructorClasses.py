# Definición de una classe Python y su constructor
class Persona:

    # Este es el constructor de la clase
    def __init__(self, nombre='', edad=0):
        self.nombre = nombre
        self.edad = edad

    def datos(self):
        print(f'Nombre = {self.nombre}, Edad = {self.edad}')

ana = Persona('Ana', 27)
ana.datos()

luis = Persona('Luis', 29)
luis.datos()

sin_edad = Persona('Luca')
sin_edad.datos()

sin_datos = Persona()
sin_datos.datos()

nueva_clase = Persona(edad=33, nombre='Carlos')
nueva_clase.datos()


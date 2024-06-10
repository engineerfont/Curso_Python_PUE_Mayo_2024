# Definición de una classe Python y su constructor
class Persona(object):

    def __init__(self):
        self.nombre = ''
        self.edad = 0

    def datos(self):
        print(f'Nombre = {self.nombre}, Edad = {self.edad}')


ana = Persona()
ana.nombre = 'Ana'
ana.edad = 27
ana.datos()

luis = Persona()
luis.nombre = 'Luis'
luis.edad = 29
luis.datos()

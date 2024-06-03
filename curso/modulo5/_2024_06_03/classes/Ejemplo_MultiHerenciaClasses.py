class Volar:

    def __init__(self):
        self.nombre = ''

    def mostrar(self):
        print('Puedo volar')

class Nadar:

    def mostrar(self, a):
        print('Puedo nadar')

class PezVolador(Nadar, Volar):
    pass

pez = PezVolador()
pez.mostrar()

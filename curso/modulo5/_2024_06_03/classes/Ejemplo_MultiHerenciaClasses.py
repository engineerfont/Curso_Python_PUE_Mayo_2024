class Volar:

    def __init__(self):
        self.nombre = ''

    def mostrar(self):
        print('Puedo volar')


class Nadar:

    def mostrar(self, a):
        print('Puedo nadar ' * a)


class PezVolador(Volar, Nadar):
    pass


pez_volador = PezVolador()
pez_volador.mostrar()

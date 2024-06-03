class Vehiculo:
    # Variables de clase públicas o propiedades
    marca = ''
    modelo = ''

    # Método constructor de la clase
    def __init__(self, ruedas=4, color='Negro'):
        # Variables de instancia públicas
        self.ruedas = ruedas
        self.color = color

    def mostrar_nombre_clase(self):
        print(f'Nombre clase = {self.__class__}')

    def mostrar_nombre_modulo(self):
        print(f'Nombre módulo = {self.__module__}')

    def mostrar_propiedades(self):
        print(f'Propiedades class = {self.__dict__}')

coche = Vehiculo()
coche.mostrar_nombre_clase()
coche.mostrar_nombre_modulo()
coche.mostrar_propiedades()

moto = Vehiculo(2, 'Blanco')
moto.mostrar_nombre_clase()
moto.mostrar_nombre_modulo()
moto.mostrar_propiedades()


class Vacia:
    pass

vacia = Vacia()
print(vacia.__dict__)
class Persona(object):

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad =edad

    def mostrar(self):
        print(f'Nombre = {self.nombre}, Edad = {self.edad}')


class Xoan(Persona):

    # Método que sobreecribe al método padre o madre
    def mostrar(self):
        n = int(input('Número => '))
        print(n ** 2)


xoan = Xoan()

xoan.mostrar()



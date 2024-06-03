class Persona:

    __fecha = ''

    def __init__(self, nombre='', edad=0):
        self.nombre = nombre
        self.edad = edad
        self.__nacimiento = ''

    def datos(self):
        return f'Nombre = {self.nombre}, Edad = {self.edad}'

    def __mostrar_nacimiento(self):
        print(f'Nacimiento = {self.__nacimiento}')

class Usuario(Persona):

    def __init__(self, nombre='', edad=0):
        super().__init__(nombre, edad)

    def ver_nacimiento(self):
        print(f'Nacimiento = {self.__nacimiento}')

u = Usuario()
print(u.datos())

#print(u.__fecha)
#u.__mostrar_nacimiento()
u.ver_nacimiento()


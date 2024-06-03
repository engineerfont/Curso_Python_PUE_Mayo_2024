class Nueva:
    pass

class Persona:

    def __init__(self, nombre='', edad=0):
        self.nombre = nombre
        self.edad = edad
        if edad > 17:
            self.mayor = True
        else:
            self.menor = True

'''ana = Persona(edad = 19)
print(hasattr(ana, 'menor'))'''


class Usuario(Persona):

    def __init__(self, nombre='', edad=0, titulo=''):
        super().__init__(nombre, edad)
        self.titulo = titulo

class Otra(Nueva):
    pass


user = Usuario()
user2 = Usuario()

otra = Otra()
if isinstance(user, Persona):
    print('Es instancia')
else:
    print('No es instancia')

if issubclass( Usuario, Persona):
    print('Es subclase')
else:
    print('No es subclase')

user3 = user
if user is user3:
    print('Mismo objeto')
else:
    print('No es el mismo objeto')

'''print(user)
print(user3)'''


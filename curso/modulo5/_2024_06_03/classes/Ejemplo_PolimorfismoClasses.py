class Persona:

    def __init__(self, nombre='', edad=0):
        self.nombre = nombre
        self.edad = edad

    def datos(self):
        return f'Nombre = {self.nombre}, Edad = {self.edad}'

class Usuario(Persona):

    def __init__(self, nombre='', edad=0, titulo=''):
        super().__init__(nombre, edad)
        self.titulo = titulo

    def datos(self):
        #datos = super().datos()
        #return f'{datos}, Titulo = {self.titulo}'
        return len(self.nombre)


u = Usuario('Xoan', 53, 'CEO')
print(u.datos())


import os

# Definición de una classe Python y su constructor
class Persona:

    def __init__(self, nombre='', edad=0):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'Nombre = {self.nombre}, Edad = {self.edad}'
    
    def __eq__(self, other):
        return self.nombre == other.nombre and self.edad == other.edad
    '''
    def __lt__(self, other):
        return self.edad > other.edad

    def datos(self):
        print(f'Nombre = {self.nombre}, Edad = {self.edad}')
    '''

persona1 = Persona('Luca')
persona2 = Persona('Luca')

if persona1 == persona2:
    print('Son iguales')
else:
    print('Son distintos')

#print('Hola => ' + str(persona1))

#print(persona1.__dir__()

'''
class Point:

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x = {self.x}, y = {self.y}'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __del__(self):
        with open('c:/datasets/data/c1.txt', 'a') as fichero:
            fichero.write(str(self.x) + ', ' + str(self.y) + '\n')


c1 = Point(10, 10)
c2 = Point(20, 40)
c3 = c1 + c2
print(c3)

del c1
'''
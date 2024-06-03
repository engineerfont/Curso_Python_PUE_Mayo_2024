# Definición de una classe Python y su constructor
class Persona:

    #self.pais = 'Portugal'

    ciudad = 'Leon'

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def datos(self):
        self.pais = 'Portugal'
        print(f'Nombre = {self.nombre}, Edad = {self.edad}')

    def __show_nombre(self):
        print(self.nombre)

    def show_edad(self):
        print(self.edad)
        self.__show_nombre()

#pedro = Persona()

ana = Persona('Ana', 37)
'''print(ana.ciudad)
ana.datos()
print(ana.pais)'''
ana.show_edad()

'''luis = Persona('Luis', 39)
print(luis.ciudad)
luis.datos()'''

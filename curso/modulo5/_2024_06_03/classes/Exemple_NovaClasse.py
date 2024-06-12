class NuevaClase(object):

    MAYOR = True
    __EDAD = 23

    def __init__(self, nombre):
        self.nombre = nombre
        self.__altura = 1.8
        print(self.__altura)




print(NuevaClase.MAYOR)
#print(NuevaClase.__EDAD)
clase_0 = NuevaClase(45)
clase_1 = NuevaClase('Lucia')
clase_2 = NuevaClase('Marcos')

print(clase_1.nombre)
print(clase_2.nombre)
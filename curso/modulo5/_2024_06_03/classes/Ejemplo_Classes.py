# Definición y características de classes en Python
class Clase(object):
    # Variable de clase pública
    atributo_clase = "Hola"   # Accesible desde el exterior

    # Variable de clase privada
    __atributo_clase = "Hola" # No accesible

    # Método privado de clase
    def __mi_metodo(self): # No accesible desde el exterior
        print("Haz algo")

    # Método público de clase
    def metodo_normal(self): # Accesible desde el exterior
        self.__mi_metodo()


mi_clase = Clase()
print(mi_clase.atributo_clase)
#print(mi_clase.__atributo_clase)
mi_clase.metodo_normal()
#mi_clase.__mi_metodo()

# Definición y características de classes en Python
class Clase(object):
    # Variable de clase pública
    atributo_clase = "Hola"   # Accesible desde el exterior

    # Variable de clase privada
    __atributo_clase_nueva = "Hola" # No accesible

    # Método privado de clase
    def __mi_metodo(self): # No accesible desde el exterior
        self.nombre = 'Ana' # Esto es una variable de instancia de clase
        self.__password = '1234'
        print("Haz algo")

    # Método público de clase
    def metodo_normal(self): # Accesible desde el exterior
        self.__mi_metodo()

ejemplo = Clase() # Crear una instancia de una clase determinada

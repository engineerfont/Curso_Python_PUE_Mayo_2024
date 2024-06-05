# función decoradora que agrega una función a la clase
def saludo(clase):
    def saludar(self):
        print(f"Hola {self.nombre}")

    clase.msg = saludar
    return clase

# función decoradora que agrega una propiedad a la clase
def es_mayor_de_edad(clase):

    @property
    def get_mayor_de_edad(self):
        return self.edad > 17

    clase.es_mayor = get_mayor_de_edad
    return clase

@saludo
@es_mayor_de_edad
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

lucia = Persona('Lucia', 32)
# lucia.msg()

print(lucia.es_mayor)

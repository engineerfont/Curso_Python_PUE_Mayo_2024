# función decoradora que agrega una función a la clase
def saludo(cls):
    def saludar(self):
        print(f"Hola {self.nombre}")

    cls.saludar = saludar
    return cls

# función decoradora que agrega una propiedad a la clase
def es_mayor_de_edad(cls):
    @property
    def mayor_de_edad(self):
        return self.edad > 17

    @mayor_de_edad.setter
    def mayor_de_edad(self, value):
        self.edad = value

    cls.es_mayor = mayor_de_edad
    return cls

def validate_attributes(cls):
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        if not self.nombre:
            raise ValueError("Se requiere el atributo 'nombre'")
        if self.edad < 0 or self.edad > 100:
            raise ValueError("Número de edad no válida")

    cls.__init__ = new_init
    return cls

@saludo
@es_mayor_de_edad
@validate_attributes
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

carla = Persona(None, -1)
print(carla.nombre)
print(carla.es_mayor)

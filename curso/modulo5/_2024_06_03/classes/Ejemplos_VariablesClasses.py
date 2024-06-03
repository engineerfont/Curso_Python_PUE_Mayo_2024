class Persona:
    # Variable de clase pública
    poblacion = 'Barcelona'
    # Variable de clase privada
    __es_mayor = False

    # Este método representa el constructor de una clase
    def __init__(self):
        # Variables de instancia públicas
        self.nombre = ''
        self.edad = 0
        #Variable de instancia privada
        self.__nacimiento = ''

    # Método público
    def datos(self):
        print(f'Nombre = {self.nombre}, Edad = {self.edad}')

    # Método privado
    def __datos_personales(self):
        print(f'Nombre = {self.nombre}, Edad = {self.edad}, Nacimiento = {self.__nacimiento}')

ana = Persona()
ana.nombre = 'Ana'
ana.edad = 28
ana.datos()
#ana.__datos_personales()
print(ana.poblacion)
#print(ana.__es_mayor)

print("Mostrar variable de clase =>", Persona.poblacion)
print(Persona.nombre)
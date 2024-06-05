def decorador_clase(clase):
    clase.nombre = 'Lorena'
    clase.edad = 28
    return clase


@decorador_clase
class MiClase:
    pass


lorena = MiClase()
print(lorena.nombre)
print(lorena.edad)

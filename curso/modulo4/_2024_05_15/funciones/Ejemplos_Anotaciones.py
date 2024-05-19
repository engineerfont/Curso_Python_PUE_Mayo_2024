# Anotaciones en funciones
# Dicha funcionalidad nos permite añadir metadatos a las funciones,
# indicando los tipos esperados tanto de entrada como de salida.

# Tipos de anotaciones
# Anotación             Tipo
# ---------             --------------------------------------
# int                   Numérico entero
# float                 Numérico real
# complex               Numérico complejo
# str                   Texto o cadena
# bool                  Booleano
# list[int]             Lista de números enteros
# tuple[int]            Tupla de números enteros
# set[int]              Conjunto de números enteros
# dict[str:int]         Diccionario 'key' de texto, 'value' número entero
# None                  Nada o sin tipo

def multiplicar(a: int, b: float) -> dict[str,dict]:
    return a * b

print("Anotaciones =>", multiplicar(3,4))

print('-' * 80)


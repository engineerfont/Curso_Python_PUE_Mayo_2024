# Python maneja literales y variables
# Tipos de literales
# - Numéricos: (int, float, complex)
# - Booleanos: True, False
# - Texto: 'Xoan', "Pontevedra"
# - Colecciones: (list, set, tuple, dict)
# - Objetos

# Identificadores, se utilizan para definir los nombres de las variables,
# funciones y clases

# Identicadores válidos: deben de empezar por letra (alfabeto inglés) o guión bajo (_)
# seguido de letras o números o guiones

edad = 27               # Variable numérica entera
print(edad)
print(type(edad))
altura = 1.89           # Variable numérica real
complejo = 4.8 + 2.4j   # Variable numérica compleja
mayor = True            # Variable booleana
nombre = "Xoan"         # Variable de texto o cadena
numeros = [2,3,4]       # Variable tipo de colección lista

edad = "Barcelona"
print(edad)
print(type(edad))

# Sintaxis de escritura de los identificadores:
# - Snake Case: Se utiliza para los identificadores de variables y funciones, y todas las
#   letras deben de estar en minúsculas
#   Ejemplo: edad_maxima, peso_altura

# - Camel Case: Se utiliza para los identificadores de clases, la primera letra del
#   identificador irá en mayúsculas y después minúsculas
#   Ejemplo: DataFile, DataTemp

# Las variables que nunca de cambian de valor o constantes los identificadores se
# escriben en mayúsculas

# Python es Case Sensitive, es decir, distingue mayúsculas de minúsculas
edad = 'xoan'
EDAD = 20
Edad = 13.6
eDaD = False

print(Edad)

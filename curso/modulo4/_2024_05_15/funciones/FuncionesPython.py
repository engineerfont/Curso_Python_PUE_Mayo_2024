# Ejemplos de funciones en Python

# Cualquier función tendrá un nombre, unos argumentos o parámetros de
# entrada, un código a ejecutar y unos parámetros de salida. Al igual que
# las funciones matemáticas, en programación nos permiten realizar
# diferentes operaciones con la entrada, para entregar una determinada
# salida que dependerá del código que escribamos dentro.

# Las funciones en Python pueden o no, devolver valores

# Una función sin parámetros de entrada ni parámetros de salida.
def primera():
    print('Primera función en Python')

primera()

print('-' * 80)

# Una función con parámetros de entrada y devuelve un valor
def resta(a, b):
    return a - b

print("Resta =>", resta(10, 3))

print('-' * 80)

# Llamar a funciones con argumentos por nombre
def dividir(a, b):
    return a / b

rdo1 = dividir(6, 4)
rdo2 = dividir(a=4, b=6)
rdo3 = dividir(b=6, a=4)
print("rdo1 =>", rdo1)
print("rdo2 =>", rdo2)
print("rdo3 =>", rdo3)

print('-' * 80)

# Función que devuelve un valor o ninguno 'None
def longitud(msg):
    if len(msg) > 2:
        return len(msg)

rdo1 = longitud('Mi nombre')
rdo2 = longitud('M')
print("rdo1 =>", rdo1)
print("rdo2 =>", rdo2)

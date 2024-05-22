# Ejemplos de matrices en Python

matriz = [[2, 3], [3, 46], [5, 6, 8]]

# Recorriendo una matriz por elementos
for filas in matriz:
    for columnas in filas:
        print(columnas)

print('-' * 80)

# Recorriendo una matriz por posición del elemento
for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        print(matriz[f][c])

print('-' * 80)

# Comprobando si los elementos de las filas de una matriz son listas
matriz = [[2, 3], [3, 46], 'nueva', False, [5, 6, 8]]
for fila in matriz:
    if type(fila) == list:
        print('Es una lista')
    else:
        print('No es una lista')

# Mostrar los elementos de una matriz hasta un elemento determinado
hasta = 46
for filas in matriz:
    for elemento in filas:
        if elemento == hasta:
            break
        else:
            print(elemento)
    else:
        continue
    break

# Comprobar si un determinado elemento está dentro de una lista
matriz = [[2, 3], [3, 46], [5, 6, 8]]
existe = 46 in matriz
print('Existe =>', existe)

"""
p = 90
x = 1.45
b = False
c = 'cadena'
print(type(p))
print(type(x))
print(type(b))
print(type(c))
"""



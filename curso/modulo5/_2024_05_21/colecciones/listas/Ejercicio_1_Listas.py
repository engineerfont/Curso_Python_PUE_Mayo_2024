# Pedir por teclado valores de dos listas

# Valores de la primera lista, se agregan valores hasta introducir el '0'
# Valores de la segunda lista, se agregan valores hasta introducir el '0'

# Realizar la suma de los elementos de las dos listas y mostrar en pantalla
# 5, 4, 8, 9
# 6, 3
# 2, 5, 3, 4
# -------------
# 13, 12

# Primera   Segunda     Tercera     Suma
#    5        6           2         5 + 6 + 2   13
#    4        3           5         4 + 3 + 5   12
#    8                    3
#    9                    4

def getLista():
    lista = list()
    x = -1
    while x != 0:
        x = int(input('Número: '))
        if x == 0:
            continue
        lista.append(x)
    return lista

ejemplo = ([1,2,3,4], [2,3,4,], [3,4])
def suma_listas(*listas):
    parametros = [list(lista) for lista in listas]
    if len(parametros) < 1:
        return []
    minimo = len(parametros[0])
    for g in listas:
        if len(g) < minimo:
            minimo = len(g)
    rdo = []
    for x in range(minimo):
        suma = 0
        for num in range(len(parametros)):
            suma += listas[num][x]
        rdo.append(suma)
    return rdo

'''primera = getLista()
segunda = getLista()

tercera = suma_listas(primera, segunda)
print(tercera)'''

r1 = [2, 3]
r2 = [1, 1]
r3 = [1, 2, 3]
r5 = {1, 2}
r6 = (9, 9, 7)

# [4, 6]
r4 = suma_listas(r1, r5, r6)
print(r4)

# Las funciones también pueden contener funciones internas

def suma_doble(numeros):
    def suma():
        suma = 0
        for j in numeros:
            suma += j
        return suma

    if len(numeros) > 0:
        return suma() * 2
    return 0


rdo = suma_doble([10, 20])
print("suma_doble =>", rdo)

print('-' * 80)


def suma_caracteres(palabras):
    caracteres = 0

    def longitud(palabra):
        return len(palabra)

    for palabra in palabras:
        caracteres += longitud(palabra)

    return caracteres


idiomas = ['inglés', 'francés', 'italiano']
letras = {'x' * n for n in range(1, 5)}

rdo1 = suma_caracteres(['java', 'python', 'c++'])
rdo2 = suma_caracteres(idiomas)
rdo3 = suma_caracteres(letras)
print('suma_caracteres =>', rdo1)
print('suma_caracteres =>', rdo2)
print('suma_caracteres =>', rdo3)

print('-' * 80)


# Funciones que devuelven otras funciones
def operaciones(tipo):
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    def dividir(a, b):
        return a / b

    def multiplicar(a, b):
        return a * b

    if tipo == 1:
        return sumar
    if tipo == 2:
        return restar
    if tipo == 3:
        return dividir
    if tipo == 4:
        return multiplicar


opera1 = operaciones(1)
opera2 = operaciones(2)
opera3 = operaciones(3)
opera4 = operaciones(4)
print(opera1(6, 3))
print(opera2(6, 3))
print(opera3(6, 3))
print(opera4(6, 3))

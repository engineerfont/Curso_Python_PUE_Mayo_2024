import random


def generar_numeros():
    yield 4
    yield 5
    yield 6


def generar_frases(numero):
    for i in range(numero):
        yield f'Frase numero {i + 1}'


def generar_numeros_aleatorios(numeros):
    return (    random.randint(1, 1000000) for _ in range(numeros)    )


def ejemplo_nuevo_generador():
    g = generar_numeros()
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))


def ejemplo_generar_frases():
    frases = generar_frases(20)
    print(next(frases))
    print(next(frases))
    for f in frases:
        print(f)
    for k in frases:
        print(k)


def ejemplo_generar_aleatorios():
    for n in generar_numeros_aleatorios(100):
        print(n)


class Cuadrado(object):

    def __init__(self, numeros):
        self.i = 0
        self.numeros = numeros

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > self.numeros:
            raise StopIteration
        result = self.i ** 2
        self.i += 1
        return result


def ejemplo_generar_cuadrados():
    elevar = Cuadrado(10)
    for n in elevar:
        print(n)


#ejemplo_nuevo_generador()
#ejemplo_generar_frases()
#ejemplo_generar_aleatorios()
ejemplo_generar_cuadrados()

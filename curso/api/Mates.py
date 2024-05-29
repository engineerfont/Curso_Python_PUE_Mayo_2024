def suma(a, b):
    return a + b


def sumatorio(*numeros):
    suma = 0
    for n in numeros:
        suma += n
    return suma

def sumatorio2(*numeros):
    return sum(numeros)

# De forma recursiva
def sumatorio3(*numeros):
    pass

def pow2(exponente):
    return (1 << exponente) if exponente >= 0 else 0 # (exponente >= 0 ? (1<<exponente) : 0)

def suma_valores(*parms1, **params2):
    suma = sum(parms1)
    for key, value in params2.items():
        suma += value
    return suma

def es_bisiesto(anho):
    return anho % 400 == 0 or (anho % 100 != 0 and anho % 4 == 0)

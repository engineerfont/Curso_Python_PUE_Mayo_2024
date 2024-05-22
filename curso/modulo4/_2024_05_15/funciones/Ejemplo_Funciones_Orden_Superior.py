# Función de orden superior que recibe como primer argumento una función
# y los restantes argumentos representan valores que se le enviarán a la función
def operacion(funcion, param1, param2):
    return funcion(param1, param2)

def multi(r, m):
    return r * m

def divide(u, m):
    return u // m

multiplicar = operacion(multi, 8, 6)
dividir = operacion(divide, 78, 4)

print(multiplicar)
print(dividir)

print('-' * 90)

#----------------------------------------------------------------------

# Función de orden superior que devuelve una función
def tipo(t):
    if t == 1:
        return multi
    else:
        return divide

multiplicar = tipo(1)
dividir = tipo(2)

print(multiplicar(3, 4))
print(dividir(23, 5))

print(tipo(1)(3, 4))
print(tipo(2)(23, 5))

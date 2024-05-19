# Definir una función que reciba un valor númerico entero
# y el tipo de números a devolver, como una lista, utilizando
# for comprenhension
# La función devolverá números entre '0' y el valor que reciba y,
# los números a devolver serán los siguientes:
# Si el tipo = 0, devuelve todos los números entre '0' y el valor
# Si el tipo = 1, devuelve todos los números pares entre '0' y el valor
# Si el tipo = 2, devuelve todos los números impares entre '0' y el valor
def listas(valor, tipo):
    if tipo == 1:
        return [k for k in range(0, valor + 1, 2)]
    elif tipo == 2:
        return [k for k in range(1, valor + 1, 2)]
    return [k for k in range(valor + 1)]

numero = int(input('Número '))

print(listas(numero, 0)) # [0,1,2,3,4,5,6,7,8]
print(listas(numero, 1)) # [0, 2, 4, 6, 8]
print(listas(numero, 2)) # [1, 3, 5, 7]


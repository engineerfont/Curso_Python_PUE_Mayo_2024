def sumatorio(*numeros):
    suma = 0
    for n in numeros:
        suma += n
    return suma

s = sumatorio(1,2,3,4,3,4,4,4,5,56,56,6,6,6,6,456,5,645,6,456,456,3456,34,3)
print("Suma =", s)

def sum(n, b=5, *h):
    suma = 0
    for n in h:
        suma += n
    return n + b + suma

print(sum(4))


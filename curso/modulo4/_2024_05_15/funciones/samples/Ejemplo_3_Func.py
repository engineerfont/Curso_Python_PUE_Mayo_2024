def sumatorio(hasta):
    suma = 0
    for n in range(1, hasta + 1):
        suma += n
    return suma

rdo = sumatorio(5000)
print(rdo)
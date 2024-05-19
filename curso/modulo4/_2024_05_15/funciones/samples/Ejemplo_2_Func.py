def sumatorio():
    suma = 0
    for n in range(1, 101): # 1,2,3,4,5,6,7,8, .. 100
        suma += n
    return suma

rdo = sumatorio()
print(rdo)
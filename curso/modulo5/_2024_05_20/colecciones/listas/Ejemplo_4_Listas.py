lista = []
numeros = [0,1,2,3,4,5,6,7,8,9,10]
for k in numeros:
    if k % 2 == 0:
        lista.append(k)

# for comprehension
lista2 = [k for k in numeros if k % 2 == 0]
print(lista2)

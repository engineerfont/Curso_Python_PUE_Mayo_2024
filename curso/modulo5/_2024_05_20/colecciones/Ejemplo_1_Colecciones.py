# Ejemplo de for comprenhension

pares = []
for x in range(0, 100, 2):
    pares.append(x)
# print(pares)

# Ejemplo anterior pero con for comprenhension
pares = [x for x in range(0, 100, 2)]
print(pares)

cuadrados = [b ** 2 for b in range(1, 11)]
print(cuadrados)


# cuadrados_impares =
# print([m ** 2 for m in range(1, 20) if m % 5 == 0])

def cuadrados(desde, hasta):
    return [h ** 2 for h in range(desde, hasta + 1)]


print(cuadrados(11, 20))

conjun = {n for n in range(4)}
print(conjun)

lista = ['R', 'Java', 'Python', 'Scala', 'Go']
dicci = {p: len(p) for p in lista}
print(dicci)

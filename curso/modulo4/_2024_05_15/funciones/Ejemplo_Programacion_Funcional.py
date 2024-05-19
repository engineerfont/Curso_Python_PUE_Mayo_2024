lenguajes = ['python', 'java', 'go', 'javascript']

mayus = [p.upper() for p in lenguajes]

def numeros(palabra):
    return len(palabra)

print(mayus)
mapa = list(map(lambda k: k.upper(), lenguajes))
print(mapa)
mapa2 = list(map(numeros, lenguajes))
print(mapa2)


veces = 0
divisibles = 0
while veces < 10:
    numero = int(input('Introduzca un número '))
    if numero % 7 == 0:
        divisibles = divisibles + 1
    veces = veces + 1
print('Total números divisibles entre 7', divisibles)
veces = 0
cincos = 0
while veces < 10:
    numero = int(input('Introduzca un número '))
    if numero > 5:
        cincos = cincos + 1
    veces = veces + 1
print('Total números mayor que 5', cincos)

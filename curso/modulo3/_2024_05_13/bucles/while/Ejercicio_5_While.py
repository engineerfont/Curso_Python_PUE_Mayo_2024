total_pares = 0
total_impares = 0
suma_pares = 0
suma_impares = 0
numero = 4534
while numero != 0:
    numero = int(input('Introduzca un valor '))
    if numero != 0:
        if numero % 2 == 1:
            total_impares += 1
            suma_impares += numero
        else:
            total_pares += 1
            suma_pares += numero
print('total pares', total_pares)
print('total impares', total_impares)
print('Suma de pares', suma_pares)
print('Suma de impares', suma_impares)

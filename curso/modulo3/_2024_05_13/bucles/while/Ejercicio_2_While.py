numeros = int(input('¿Cuántos números? '))
sumatorio = 0
while numeros > 0:
    numero = int(input('Introduzca un número '))
    sumatorio = sumatorio + numero
    numeros = numeros - 1
print('El sumatorio es', sumatorio)

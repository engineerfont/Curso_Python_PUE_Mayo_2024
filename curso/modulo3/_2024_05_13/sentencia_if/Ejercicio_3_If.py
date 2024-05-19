print('Introduzca un número')
numero = int(input())
print('Introduzca el divisor')
divisor = int(input())
if divisor == 0:
    print('Error: Esta división no se puede realizar')
else:
    rdo = numero / divisor
    print('La división es ', rdo)

# Mostrar la tabla de multiplicar de un determinado número
n = int(input('Número '))
for numero in range(1, 11):
    print(numero, '*', n, '=', numero * n)

n = int(input('¿Cuántos números quieres introducir? '))  # 5
impares = []
pares = []
for r in range(n):
    numero = int(input('Número '))
    if numero % 2 == 1:
        impares.append(numero)
    else:
        pares.append(numero)

print('Lista de impares =', impares)
print('Lista de pares =', pares)


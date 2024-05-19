# Adivinar un número
import random

aletorio = random.randint(1, 10000) # 800

# Número entre 1 y 1000
# 600
# Número entre 600 y 1000
# 900
# Número entre 600 y 900
# 700
# Número entre 700 y 900
# 800
# Has acertado, número de intentos 4
intentos = 0
numero = 0
maximo = 10000
minimo = 1
while numero != aletorio: # 800
    print("Número entre", minimo, " y", maximo)
    numero = int(input('Numero: '))
    intentos += 1
    if numero < aletorio:
        minimo = numero
    elif numero > aletorio:
        maximo = numero

print("Enhorabuena, nº de intentos ", intentos)


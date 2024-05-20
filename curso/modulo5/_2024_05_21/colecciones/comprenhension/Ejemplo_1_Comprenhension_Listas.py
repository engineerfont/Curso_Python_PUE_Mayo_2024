# Solicitar por teclado un número y definir una función
# que reciba el número introducido por teclado y devuelva
# una lista con los números comprendidos entre '0' y
# el número introducido, utilizando for comprenhension

numeros = [3,4,6,7,8]
print(numeros)

dobles = tuple([n * 2 for n in numeros])
print(dobles)

numeros = {n for n in range(1, 10)}
print(numeros)

{3:3, 4:4, 6:6, 7:7, 8:8}
diccionario = {n : n for n in numeros}
print(diccionario)

generador = (n * 2 for n in numeros)

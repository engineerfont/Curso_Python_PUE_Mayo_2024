# Solicitar por teclado un número y definir una función
# que reciba el número introducido por teclado y devuelva
# una lista con los números comprendidos entre '0' y
# el número introducido, utilizando for comprenhension

def lista_numeros(valor):
    return [k for k in range(valor + 1)]

n = int(input('Número '))   # 4
lista = lista_numeros(n)
print(lista) # [0,1,2,3,4]

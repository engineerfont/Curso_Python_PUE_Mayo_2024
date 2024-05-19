# Tipos de literales numéricos, booleanos
# - Numéricos enteros: 1, 2
# - Numéricos reales; 1.78, 23.8
# - Numéricos complejos: 2.7+2.5j, 7.6-4.3j

edad = 20
print(type(edad))
altura = 1.83
print(type(altura))
complejo = 7.6-4.3j
print(type(complejo))
sedad = "20"
saltura = "1.83"
scomplejo = "7.6-4.3j"

print(int(sedad)) # Convertir a entero
print(float(saltura)) # Convertir a real
print(complex(scomplejo)) # Convertir a complejo

scomplejo = str(complejo) # Convertir a cadena de texto
print(scomplejo)

# Tipos de literales booleanos
# - Booleano: True, False

mayor = True # Literal booleano
print(type(mayor))

menor = bool(0) # Convertir a booleano
print(menor)

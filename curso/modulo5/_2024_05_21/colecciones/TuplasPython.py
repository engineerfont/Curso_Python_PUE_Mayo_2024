# Ejemplos de tuplas en Python

# Algunas propiedades de las tuplas:

# Son ordenadas, mantienen el orden en el que han sido definidas
# Pueden ser formadas por tipos arbitrarios
# Pueden ser indexadas con [i].
# Se pueden anidar, es decir, meter una dentro de la otra.
# Son inmutables, ya que sus elementos no pueden ser modificados.

# Las tuplas en Python o tuples son muy similares a las listas, pero con
# dos diferencias. Son inmutables, lo que significa que no pueden ser
# modificadas una vez declaradas, y en vez de inicializarse con corchetes
# se hace con ().

tupla = (1, 2, 3)
print(tupla) #(1, 2, 3)

# También pueden declararse sin (), separando por , todos sus elementos.
tupla = 1, 2, 3
print(type(tupla)) #<class 'tuple'>
print(tupla)       #(1, 2, 3)

# Al igual que las listas, las tuplas también pueden ser anidadas.
tupla = 1, 2, ('a', 'b'), 3
print(tupla)       #(1, 2, ('a', 'b'), 3)
print(tupla[2][0]) #a

# Operaciones con tuplas
tupla = (1, 2, 3)
#tupla[0] = 5 # Error! TypeError

# Es posible convertir una lista en tupla haciendo uso de la función tuple()
lista = [1, 2, 3]
tupla = tuple(lista)
print(type(tupla)) #<class 'tuple'>
print(tupla)       #(1, 2, 3)

# Las tuplas se pueden recorrer como las listas
tupla = (1, 2, 3)
for t in tupla:
    print(t) #1, 2, 3

# Funciones que proporcionan las tuplas
# Función 'count' idem al 'count' de las listas
tupla = (1,2,2,1,1,1,1)
print(tupla.count(1)) # 5


# Función 'index' idem al 'index' de las listas
tupla = (1,2,2,1,1,1,1)
print(tupla.index(1))

# Descomponer una tupla en variables independientes
cociente, resta, mayor = (2.5, 10, False)
print(cociente)
print(resta)
print(mayor)


# Comprobar si un determinado valor está en una tupla
tupla = (1,2,2,1,1,1,1)
existe = 4 in tupla
print(existe)

h = 1,2,3
h = 1,2,3,4
print(h)

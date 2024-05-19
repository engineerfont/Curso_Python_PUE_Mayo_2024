# Mostrar en pantalla los primeros 'n' números impares
n = int(input('Número '))  # 87
i = 1
for b in range(1, n * 2, 2): # 0 .. 86
    print(b)

# Funcionalidad de range
# esta función devuelve una serie o lista o colección de valores
# Tiene tres formatos
# - range(8)            # 0, 1, 2, 3, 4, 5, 6, 7
# - range(87, 93)       # 87, 88, 89, 90, 91, 92
# - range(87, 93, 2)    # 87, 89, 91

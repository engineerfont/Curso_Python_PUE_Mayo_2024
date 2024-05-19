# valor representa el número
# El parámetro valor es de tipo numérico entero
# El parámetro caracter es de tipo string o cadena o texto
def padding(valor, caracter, posiciones, tipo_padding):
    cad = str(valor)  # Convertir a cadena
    if len(cad) >= posiciones:
        return cad
    ceros = posiciones - len(cad)
    if tipo_padding == True:
        for y in range(ceros):
            cad = caracter + cad
    else:
        for y in range(ceros):
            cad = cad + caracter  # cad += caracter
    return cad

c = padding('-', 9, '0', True)
print(c)

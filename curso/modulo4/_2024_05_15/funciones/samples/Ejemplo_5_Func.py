# El primer parámetro representa una cadena de texto
# El segundo parámetro representa el número veces a repetir
# la cadena de texto
def repetir(letra, veces):
    cad = ''
    for k in range(veces):
        cad += letra
    print(cad)

h = 23
repetir('-', 40)
print(h)
repetir('-', 40)

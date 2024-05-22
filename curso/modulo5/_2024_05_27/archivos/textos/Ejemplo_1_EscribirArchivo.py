from os import strerror

def escribir_lineas(nombre, numero=20):
    try:
        fichero = open(nombre, 'w')
        for n in range(1, numero + 1):
            fichero.write(f'Línea número {n}\n')
        fichero.close()
    except IOError as e:
        print(strerror(e.errno))


def escribir_colecciones(nombre, coleccion):
    try:
        fichero = open(nombre, 'w')
        fichero.writelines(coleccion)
        fichero.close()
    except IOError as e:
        print(strerror(e.errno))

'''try:
    fichero = open('c:/datasets/data/ejemplo2.txt', 'w')
    for x in range(4):
        fichero.write('Alicante\n')
    fichero.close()
except:
    print('Error de escritura')'''

escribir_lineas('c:/datasets/data/ejemplo2.txt', 30)

nombres = ['Ana', 'Pepa', 'Juan']
nombres_con_salto = [n + '\n' for n in nombres]
escribir_colecciones('c:/datasets/data/colecciones.txt', nombres_con_salto)

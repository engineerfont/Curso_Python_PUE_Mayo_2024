# dado el dataset, utilizar los siguientes archivos: 'nombres.data' y 'apellidos.data'
# definir una función que recibe dos parámetros de entrada indicando el número de nombres
# masculinos y el número de nombres femeninos, devolviendo una lista con los nombres
# generados

import curso.api.Ficheros as Files
import random

def personas(hombres, mujeres):
    nombres = Files.list_file_text('c:/datasets/data/nombres.data', 'utf-8')[1:]
    nombres_masculinos = [nombre.split(';')[0] for nombre in nombres if nombre.strip().endswith('h')]
    nombres_femeninos = [nombre.split(';')[0] for nombre in nombres if nombre.strip().endswith('m')]
    #print(len(nombres_femeninos))
    apellidos = Files.list_file_text('c:/datasets/data/apellidos.data', 'utf-8')[1:]
    personas = []
    for n in range(mujeres):
        aletorio = random.randint(0, len(apellidos) - 1)
        apellido1 = apellidos[aletorio]
        aletorio = random.randint(0, len(apellidos) - 1)
        apellido2 = apellidos[aletorio]
        aletorio = random.randint(0, len(nombres_femeninos) - 1)
        nombre = nombres_femeninos[aletorio]
        personas.append(nombre+ ' ' + apellido1.strip() + ' ' + apellido2.strip())
    for n in range(hombres):
        aletorio = random.randint(0, len(apellidos) - 1)
        apellido1 = apellidos[aletorio]
        aletorio = random.randint(0, len(apellidos) - 1)
        apellido2 = apellidos[aletorio]
        aletorio = random.randint(0, len(nombres_masculinos) - 1)
        nombre = nombres_masculinos[aletorio]
        personas.append(nombre+ ' ' + apellido1.strip() + ' ' + apellido2.strip())
    random.shuffle(personas)
    return personas

personas = personas(5,5)
print(personas)

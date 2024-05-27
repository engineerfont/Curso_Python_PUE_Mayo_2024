# Dado el dataset, abrir el archico 'provincias.data', leer todo su contenido
# y mostrar únicamente el nombre de la provincia.

import curso.api.Ficheros as File

datos = File.list_file_text('c:/datasets/data/provincias.data')[1:]
for provincia in datos:
    print(provincia.split(';')[1])


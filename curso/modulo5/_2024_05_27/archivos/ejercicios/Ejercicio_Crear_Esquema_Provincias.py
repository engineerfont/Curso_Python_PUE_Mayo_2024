# dado el dataset leer el archivo 'provincias.data', definir una función que devuelva
# una lista con el formato indicado por el esquema del archivo

import curso.api.Ficheros as File

def data_record(filename):
    records = []
    lineas = File.list_file_text(filename)[1:]
    for linea in lineas:
        datos = linea.split(';')
        data = {}
        data['id'] =  # datos[0]
        data['provincia'] = datos[1]
        data['id_ccaa'] =  # datos[2]
        records.append(data)
    return records


data = data_record('c:/datasets/data/provincias.data')
for d in data:
    print(d)



# definir una función que recibe como parámetro el nombre de un directorio
# y la función devuelve una lista con los datos de los archivos de ese directorio
# Los datos tendrán el siguiente formato de diccionario:
# schema = {}
# schema['path'] = ruta del directorio
# schema['name'] = nombre del archivo
# schema['file'] = nombre del archivo completo (directorio+nombre archivo)
# schema['size'] = tamaño en bytes del archivo
# schema['access'] = fecha y hora de creación del archivo
# schema['last'] = fecha y hora de último acceso del archivo
# schema['create'] = fecha y hora de modificación del archivo

import os
import datetime as dt
import curso.api.Ficheros as File

def data_dir(dir, recursive=False):
    lista = []
    files = File.dir_files_tree(dir) if recursive else File.dir_files(dir)
    for file in files:
        registro = {}
        path, name = os.path.split(file)
        registro['path'] = path
        registro['name'] = name
        registro['file'] = file
        registro['size'] = os.path.getsize(registro['file'])
        segundos_access = os.path.getatime(registro['file'])
        segundos_last = os.path.getmtime(registro['file'])
        segundos_create = os.path.getctime(registro['file'])
        registro['access'] = dt.datetime.fromtimestamp(segundos_access)
        registro['last'] = dt.datetime.fromtimestamp(segundos_last)
        registro['create'] = dt.datetime.fromtimestamp(segundos_create)
        lista.append(registro)
    return lista

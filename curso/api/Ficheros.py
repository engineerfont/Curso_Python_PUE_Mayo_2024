import os
import datetime as dt

def dir_files(dir):
    return [os.path.join(dir, file) for file in os.listdir(dir) if os.path.isfile(os.path.join(dir, file))]

def dir_files_tree(dir):
    lista = []
    for (d, _, files) in os.walk(dir):
        for file in files:
            lista.append(os.path.join(d, file))
    # [os.path.join(d, file) for (d, _, files) in os.walk(dir) for file in files]
    return lista

def dir_dirs(dir):
    return [os.path.join(dir, file) for file in os.listdir(dir) if os.path.isdir(os.path.join(dir, file))]

def dir_dirs_tree(dir):
    lista = []
    for (d, _, _) in os.walk(dir):
        lista.append(d)
    # [d for (d, _, files) in os.walk(dir)]
    return lista

def data_dir(dir, recursive=False):
    lista = []
    files = dir_files_tree(dir) if recursive else dir_files(dir)
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

def list_file_text(filename, encoding='utf-8'):
    try:
        with open(filename, 'r', encoding=encoding) as fichero:
            lista = fichero.readlines()
    except:
        lista = []
    return lista

def file_text(filename, encoding='utf-8'):
    try:
        with open(filename, 'r', encoding=encoding) as fichero:
            texto = fichero.read()
    except:
        texto = ''
    return texto

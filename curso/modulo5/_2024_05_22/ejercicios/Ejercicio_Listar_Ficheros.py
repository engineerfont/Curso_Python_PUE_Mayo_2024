# Definir las siguientes funciones
# 1- Una función que devuelva los archivos de un directorio y de sus subdirectorios
# 2- Una función que devuelva los directorios de un directorio y de sus subdirectorios

# Utilizando recursividad

import os

def dir_dirs_tree(directorio, dirs=[]):
    for dir in os.listdir(directorio):
        direc = os.path.join(directorio, dir)
        if os.path.isdir(direc):
            dirs.append(direc)
            dirs = dir_dirs_tree(direc, dirs)
    return dirs

def dir_files_tree(dir, files=[]):
    for file in os.listdir(dir):
        filename = os.path.join(dir, file)
        if os.path.isfile(filename):
            files.append(filename)
        else:
            files = dir_files_tree(filename, files)
    return files

# Mostrar todos los subdirectorios de un directorio
#for f in dir_dirs_tree('c:/datasets/'):
#    print(f)

# Mostrar todos los archivos de un directorio y de todos sus subdirectorios
for f in dir_files_tree('c:/datasets/'):
    print(f)

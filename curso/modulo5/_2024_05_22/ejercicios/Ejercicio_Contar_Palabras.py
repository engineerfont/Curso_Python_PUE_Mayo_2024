# Dado un texto por teclado, mostrar en pantalla las palabras únicas
# con sus correspondientes números de apariciones

# Esto es un nuevo comentario de texto y un nuevo texto
# esto - 1
# es   -
# un   - 2
# nuevo - 2

texto = input('Texto: ')
palabras_unicas = set(texto.lower().split(' '))
print(palabras_unicas)

import curso.api.Texto as Texto

palabras = {}
for palabra in palabras_unicas:
    palabras[palabra] = len(Texto.ocurriencias(texto, palabra, []))

#palabras = {palabra: len(Texto.ocurriencias(texto, palabra, [])) for palabra in palabras_unicas}

for k,v in palabras.items():
    print(f'{k} = {v}')


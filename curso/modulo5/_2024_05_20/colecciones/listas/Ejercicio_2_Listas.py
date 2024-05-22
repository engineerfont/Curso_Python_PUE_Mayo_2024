# Dada la siguiente cadena de texto
# ' 6,7.8,-5.6+9.23j,False,None,"Barcelona" '
# Crear una lista con los valores de la cadena definiendo una función para ello

def is_float(value):
    es = True
    try:
        v = float(value)
    except:
        es = False
    return es

def is_complex(value):
    es = True
    try:
        v = complex(value)
    except:
        es = False
    return es

def is_bool(value):
    return value.lower() == 'false' or value.lower() == 'true'

def is_none(value):
    return value.lower() == 'none'

def string_to_list(texto, separador=','):
    #lista = [eval(c.capitalize()) for c in texto.split(separador)]
    '''tokens = texto.split(separador)
    for token in tokens:
        if token.isnumeric():
            lista.append(int(token))
        elif is_float(token):
            lista.append(float(token))
        elif is_complex(token):
            lista.append(complex(token))
        elif is_bool(token):
            lista.append(token.lower() == 'true')
        elif is_none(token):
            lista.append(None)
        else:
            lista.append(token.replace('"', '').replace("'", ""))'''
    return [eval(c.capitalize()) for c in texto.split(separador)]


texto = '6,7.8,-5.6+9.23j,false,none,"Barcelona"'
a = string_to_list(texto)
print(a)
print(type(a[2]))
# [6,7.8,-5.6+9.23j,False,None,"Barcelona"]

# {
# '_c1': 6,
# '_c2': 7.8,
# '_c3': -5.6+9.23j,
# '_c4': False,
# '_c5': None,
# '_c6': "Barcelona"
# }
datos = {"_c" + str(elemento[0] + 1) : elemento[1] for elemento in enumerate(string_to_list(texto))}
print(datos)

hh = [2,3,4]
enumeracion = enumerate(hh)
print(list(enumeracion))

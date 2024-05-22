# Descomposición de colecciones en series de valores

def suma(*valores):
    return sum(valores)

def mostrar(**valores):
    for k in valores:
        print(f'{k} = {valores[k]}')

# Descomposición de colecciones tipo 'list', 'tuple', 'set'
# Para descomponer una colección en series de valores utilizaremos el '*'
numeros = {2,3,4}
s = suma(*numeros)
print(s)

# Descomposición de colecciones tipo 'dict'
# Para descomponer un diccionario en series de valores utilizaremos el '**'
datos = {"nombre": "Mia", "edad": 4, "ciudad": "Burgos"}
d = mostrar(**datos)
print(d)

# Función que utiliza la descomposición de diccionarios
# para realizar reemplazos de caracteres
def to_abc(texto):
    texto = texto.lower()

    aes = {a: 'a' for a in 'áàâäã'}
    ees = {e: 'e' for e in 'éèêë'}
    ies = {i: 'i' for i in 'íìîï'}
    oes = {o: 'o' for o in 'óòôöõ'}
    ues = {u: 'u' for u in 'úùûü'}

    letters = {'ñ': 'n', 'ç': 'c', 'ÿ': 'y', 'ý': 'y'}

    special_1 = {chr(n): '' for n in range(32)}
    special_2 = {chr(n): '' for n in range(33, 48)}
    special_3 = {chr(n): '' for n in range(58, 65)}
    special_4 = {chr(n): '' for n in range(91, 95)}
    special_5 = {chr(n): '' for n in range(123, 128)}

    chars = {
        **{a: 'a' for a in 'áàâäã'}, **ees, **ies, **oes, **ues, **letters,
        **special_1, **special_2, **special_3,
        **special_4, **special_5
    }

    for k, v in chars.items():
        texto = texto.replace(k, v)

    return texto


texto = 'en BARÇA un %8 / 3 \'(a+b)\'    [ñoño]      "Àquí"    está_    yagÜe'
t = to_abc(texto)
print(t)

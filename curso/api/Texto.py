# Esta función devuelve ...
def ocurriencias(texto, palabra, palabras=[]):
    posicion = texto.lower().find(palabra.lower())
    if posicion == -1:
        return palabras
    else:
        word = texto[posicion:]
        word = word[0:word.find(' ')] if word.find(' ') != -1 else word
        palabras.append(word)
        texto = texto[posicion + len(palabra):]
        return ocurriencias(texto, palabra, palabras)


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
        **aes, **ees, **ies, **oes, **ues, **letters,
        **special_1, **special_2, **special_3,
        **special_4, **special_5
    }

    for k, v in chars.items():
        texto = texto.replace(k, v)

    return texto

def to_email(text):
    text = to_abc(text).replace(' de ', ' ') \
        .replace(' del ', ' ') \
        .replace(' el ', ' ') \
        .replace(' la ', ' ') \
        .replace(' las ', ' ') \
        .replace(' da ', ' ') \
        .replace(' das ', ' ') \
        .replace(' do ', ' ') \
        .replace(' dos ', ' ') \
        .replace(' lo ', ' ') \
        .replace(' los ', ' ')
    return '.'.join(text.split())

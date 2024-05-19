# Definir una función que devuelva una cadena de texto rellenada por la
# izquierda con un determinado carácter

def pad_left(text, width, character): # 000000001234
    if len(text) > width:
        return text
    return character * (width - len(text))

def pad2_left(text, width, character='0'): # 000000001234
    return (character * (width - len(text))) + text if len(text) > width else text


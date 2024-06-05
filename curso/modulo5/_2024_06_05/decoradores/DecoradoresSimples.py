def mayusculas(funcion):
    def wrapper():
        return funcion().upper()

    return wrapper


def saludo_python():
    return '¡hola, soy un desarrollador de Python!'


def ejemplo_decoradores():
    hola = mayusculas(saludo_python)
    print(hola())


@mayusculas
def python_english_greeting():
    return 'hi, i\'m a Python developer!'


if __name__ == '__main__':
    #ejemplo_decoradores()
    print(python_english_greeting())

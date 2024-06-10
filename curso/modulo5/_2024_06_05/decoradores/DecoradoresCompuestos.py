def mayusculas(funcion):
    def wrapper():
        return funcion().upper()

    return wrapper
    


def invertir(funcion):
    def otra():
        return funcion()[::-1]

    return otra


@mayusculas
@invertir
def saludo_python():
    return '¡hola, soy un desarrollador de Python!'


if __name__ == '__main__':
    print(saludo_python())

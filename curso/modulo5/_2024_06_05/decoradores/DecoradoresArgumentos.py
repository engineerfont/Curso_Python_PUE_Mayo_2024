import os.path
import time
#import app.python.api.Files as File

def decorar_suma(funcion):
    def wrapper11(arg1, arg2):
        print(f'Los valores a sumar son: {arg1} y {arg2}.')
        return funcion(arg1, arg2)

    return wrapper11


@decorar_suma
def suma_numeros(num_1, num_2):
    return num_1 + num_2

@decorar_suma
def resta_numeros(num_1, num_2):
    return num_1 - num_2


# ---------------------------------------------------------------------------
def multiplica_resultado(numero):
    def decorador_interno(funcion):
        def wrapper22(arg1, arg2):
            print(f'({arg1} + {arg2}) * {numero}:')
            return funcion(arg1, arg2) * numero

        return wrapper22

    return decorador_interno


@multiplica_resultado(3)
def suma_numeros_multiplicada(num_1, num_2):
    return num_1 + num_2

'''
# ---------------------------------------------------------------------------
def mi_decorador(arg):
    def decorador_interno(funcion):
        def wrapper33(a, b):
            print(arg)
            c = funcion(a, b)
            print(arg)
            return c

        return wrapper33

    return decorador_interno


@mi_decorador("Imprimer esto antes y después")
def multiplica(a, b):
    print("Entra en función multiplicar")
    return a * b


# ---------------------------------------------------------------------------
def log(fichero_log):
    def decorador_interno(funcion):
        def wrapper44(*args, **kwargs):
            directory = os.path.dirname(fichero_log)
            os.makedirs(directory, exist_ok=True)
            with open(fichero_log, 'a') as opened_file:
                output = funcion(*args, **kwargs)
                opened_file.write(f"{funcion.__name__}{args} = {output}\n")
            return output

        return wrapper44

    return decorador_interno


@log(File.FILE_LOGS)
def suma(a, b):
    return a + b


@log(File.FILE_LOGS)
def resta(a, b):
    return a - b


@log(File.FILE_LOGS)
def multiplicadivide(a, b, c):
    return a * b / c


def ejemplo_logger():
    a = suma(70, 990)
    print(a)
    print(resta(1240, 86))
    print(multiplicadivide(211, 4, 8))


# ---------------------------------------------------------------------------
def calcular_tiempo(funcion):
    def wrapper55(*args, **kwargs):
        start = time.time()
        resultado = funcion(*args, **kwargs)
        total = time.time() - start
        print(total, 'segundos')
        return resultado

    return wrapper55


@calcular_tiempo
def division(a, b):
    time.sleep(3)
    return a / b


@calcular_tiempo
def sumas_numeros(*args, **kwargs):
    time.sleep(2)
    return sum(args) + sum(kwargs.values())


# ---------------------------------------------------------------------------
def multiplicar_resultado(*argumentos):
    def decorador_interno(funcion):
        def wrapper66(*args):
            numeros = args
            numeros_multiplicar = sum(argumentos)
            print(f'sum{numeros} * {numeros_multiplicar}:')
            return funcion(*args) * sum(argumentos)

        return wrapper66

    return decorador_interno


@multiplicar_resultado(3, 4, 5)
def sumatorio(*args):
    return sum(args)
'''

if __name__ == '__main__':
    #print(resta_numeros(7, 9))
    #print(resta_numeros(9, 7))
    print(suma_numeros_multiplicada(8, 4))
    #print(multiplica(9, 9))
    #ejemplo_logger()
    #print('division =>', division(40, 4))
    #print('sumas_numeros =>', sumas_numeros(5, 5, 5, 5, a=10, b=20, c=30))
    #print(sumatorio(1, 2))
    pass

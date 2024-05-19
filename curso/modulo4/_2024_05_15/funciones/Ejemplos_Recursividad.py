# Funciones recursivas
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print('Factorial =>', factorial(6))

print('-' * 80)

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci =>", fibonacci(38))

print('-' * 80)

def sumas(n):
    if n == 1:
        return 1
    else:
        n + sumas(n - 1)

rdo = sumas(5)

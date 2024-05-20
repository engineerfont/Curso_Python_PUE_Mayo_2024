def op1(funcion, param1, param2):
    return funcion(param1, param2)

def op2(funcion, *param1, **param2):
    return funcion(*param1, **param2)

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def mul(a):
    return 6

'''x1 = op(suma, 3, 9)
print(x1)

x2 = op(resta, 7, 11)
print(x2)

x3 = op(mul, 1, 2)
print(x3)'''

def conversor(value):
    if value == 1:
        return int
    if value == 2:
        return float
    return str

d = 2
b = conversor(2)
print(b(d))



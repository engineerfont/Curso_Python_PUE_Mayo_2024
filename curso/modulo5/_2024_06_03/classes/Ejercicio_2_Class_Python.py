# Definir una clase 'Mates' con los siguientes métodos:
# - suma(a, b) -> devuelve la suma
# - multi(h, b) -> delvuelve la multiplicación

# Pedir por teclado dos valores numéricos y crear una instancia de la clase
# 'Mates' y utilizar todos sus métodos

class Mates(object):

    def suma(self, param_1, param_2):
        return param_1 + param_2

    def __multi(self, param_1, param_2):
        return param_1 * param_2

    def mul(self, k, t):
        return self.__multi(k, t)

f = int(input('N 1 => '))
k = int(input('N 2 => '))

mates = Mates()

print(mates.suma(f, k))
print(mates.mul(f, k))

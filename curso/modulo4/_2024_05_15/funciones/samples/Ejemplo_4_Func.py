def factorial(numero):
    facto = 1
    for nn in range(1, numero + 1):
        facto *= nn # facto = facto * nn
    return facto

facto = factorial(6)
print(facto)


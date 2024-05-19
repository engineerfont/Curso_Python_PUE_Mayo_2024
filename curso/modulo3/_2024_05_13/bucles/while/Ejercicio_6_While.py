div_2 = 0
div_3 = 0
div_5 = 0
div_7 = 0
n = int(input('Introduzca un valor '))
while n != 0:
    if n % 2 == 0:
        div_2 = div_2 + 1
    if n % 3 == 0:
        div_3 = div_3 + 1
    if n % 5 == 0:
        div_5 = div_5 + 1
    if n % 7 == 0:
        div_7 = div_7 + 1
    n = int(input('Introduzca un valor '))
print('divisibles entre 2', div_2)
print('divisibles entre 3', div_3)
print('divisibles entre 5', div_5)
print('divisibles entre 7', div_7)
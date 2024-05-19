print('Introduzca edad')
edad = int(input())
print('Introduzca ingresos')
ingresos = int(input())
if edad > 16:
    if ingresos >= 1000:
        print('tributa')
    else:
        print('no tributa')
else:
    print('no tributa')

if edad == 23:
    print(8)
else:
    if edad < 9:
        print(edad + 9)
    else:
        print(edad)

if edad > 23:
    if edad < 67:
        print('a')
    else:
        print('n')
else:
    if edad < 7:
        print('p')
        if edad == 2:
            print('u')
        else:
            print('r')
    else:
        print('m')
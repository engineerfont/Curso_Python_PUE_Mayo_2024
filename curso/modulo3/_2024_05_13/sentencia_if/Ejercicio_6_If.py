print('Introduzca ingresos')
ingresos = int(input())
if ingresos <= 10000:
    print('5%')
elif ingresos <= 20000:
    print('15%')
elif ingresos <= 35000:
    print('20%')
elif ingresos <= 60000:
    print('30%')
else:
    print('45%')

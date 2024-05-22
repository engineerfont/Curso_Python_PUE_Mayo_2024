try:
    y = 1 / 3
except ZeroDivisionError:
    print("¡División entre Cero!")
else:
    print('Se ejecuta el código del else')
finally:
    print('Se ejecuta el código del finally')

print("FIN.")
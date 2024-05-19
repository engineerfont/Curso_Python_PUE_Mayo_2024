def multiplica(a, b = 2):
    return a * b

print( multiplica(2, 4)  )
print( multiplica(2) )

def suma(a=3, b=2):
    return a + b

n = 67
print(suma())
print(suma(45, 10))
print(suma(a=45, b=10))
print(suma(b=10, a=45))
print(suma(b=n))
print(suma(a=30))

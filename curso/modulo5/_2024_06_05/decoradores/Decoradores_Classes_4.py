def add_sum(cls):
    cls.sum = lambda self, x, y: x + y
    return cls

def add_multi(cls):
    cls.multi = lambda self, x, y: x * y
    return cls

def add_sumatory(cls):
    cls.sumatory = lambda self, *args: sum(args)
    return cls

def add_field(field_name, default_value):
    def decorator(cls):
        setattr(cls, field_name, default_value)
        return cls

    return decorator

@add_sum
@add_multi
@add_sumatory
@add_field('nombre', 'Rosaura')
@add_field('apellidos', 'Méndez')
@add_field('edad', 36)
class MiClase(object):
    pass

sample = MiClase()
print(sample.sum(8, 8))
print(sample.multi(8, 8))
print(sample.sumatory(5, 5, 5, 5, 5))

sample2 = MiClase()
print(sample2.nombre)
print(sample2.apellidos)
print(sample2.edad)

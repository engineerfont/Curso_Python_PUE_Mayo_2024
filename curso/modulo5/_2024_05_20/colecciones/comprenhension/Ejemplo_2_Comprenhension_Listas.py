lenguajes = ['Python', 'Java', 'c++', 'Go', 'JavaScript', 'PHP']

nuevos = [programa for programa in lenguajes if len(programa) > 3]
print(nuevos)

nuevos = [programa for programa in lenguajes if programa.startswith('J')]
print(nuevos)
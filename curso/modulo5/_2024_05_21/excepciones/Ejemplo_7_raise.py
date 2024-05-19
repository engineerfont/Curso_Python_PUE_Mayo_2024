def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(4523)
except ArithmeticError:
    print("¿Que pasó? ¿Un error?")

print("FIN.")


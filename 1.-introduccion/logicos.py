# Operadores lógicos: Permiten comparar datos booleanos
# and, or y not.

# and
resultado_final = True and True
print(resultado_final)

resultado_final = True and True and False
print(resultado_final)

resultado_final = True and True and 10 > 20
print(resultado_final)


# or
resultado_final = True or True
print(resultado_final)

resultado_final = False or False or 100 > 20
print(resultado_final)

resultado_final = False or False or 10 > 20
print(resultado_final)


# combinaciones con paréntesis

resultado_final = True and (False or 5 > 10)
print(resultado_final)

resultado_final = True and (False or 50 > 10)
print(resultado_final)


# not

resultado_final = not True
print(resultado_final)

resultado_final = not False
print(resultado_final)

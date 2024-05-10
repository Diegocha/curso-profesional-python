
# función ZIP: combinar tuplas y listas
lista = [1, 2, 3, 4, 5]
tupla = (10, 20, 30, 40, 50)
resultado = zip(tupla, lista)  # -> dato tipo zip (pares ordenados)
print(resultado)

# generando una tupla
resultado = tuple(resultado)
print(resultado)  # ((10, 1), (20, 2), (30, 3), (40, 4), (50, 5))

# El orden en la función ZIP importa
lista = [1, 2, 3, 4, 5]
tupla = (10, 20, 30, 40, 50)
resultado = zip(lista, tupla)
resultado = tuple(resultado)
print(resultado)  # ((1, 10), (2, 20), (3, 30), (4, 40), (5, 50))


# Más de dos listas o tuplas
lista = [1, 2, 3, 4, 5]
tupla = (10, 20, 30, 40, 50)
lista_2 = [100, 200, 300, 400, 500]
resultado = zip(lista, tupla, lista_2)
resultado = tuple(resultado)
# ((1, 10, 100), (2, 20, 200), (3, 30, 300), (4, 40, 400), (5, 50, 500))
print(resultado)

tupla_2 = (1000, 2000, 3000, 4000, 5000)
resultado = zip(lista, tupla, lista_2, tupla_2)
resultado = tuple(resultado)
print(resultado)

tupla_3 = (1000, 2000, 3000, 4000, 5000, 6000, 7000)
resultado = zip(lista, lista_2, tupla_3)
resultado = tuple(resultado)
print(resultado)

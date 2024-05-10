# Asignar Multivariable
uno, dos, tres, cuatro = 1, 2, 3, 4
print(uno)
print(dos)
print(tres)
print(cuatro)

# Otra forma usando tupla
numeros = (1, 2, 3, 4)
uno = numeros[0]
dos = numeros[1]
tres = numeros[2]
cuatro = numeros[3]
print(uno)
print(dos)
print(tres)
print(cuatro)

# Mejor forma usando tupla
numeros = (1, 2, 3, 4)
uno, dos, tres, cuatro = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)

# Asignando todos los elementos restantes con *
# * -> crea una lista con el resto
numeros = (1, 2, 3, 4, 5, 6)
uno, dos, tres, cuatro, *resto_valores = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)
print(resto_valores)
print(type(resto_valores))

# _ -> Omitir valores del resto
uno, dos, tres, cuatro, *_ = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)

# _ -> Omitir valores dentro de la lista
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, dos, tres, cuatro, *_, nueve, diez = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)
print(nueve)
print(diez)

# lista de valores dentro de la tupla
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, dos, tres, cuatro, *resto_numeros, nueve, diez = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)
print(nueve)
print(diez)
print(resto_numeros)


# omitir valores dentro de la tupla
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, _, tres, cuatro, *_, nueve, diez = numeros
print(uno)
print(tres)
print(cuatro)
print(nueve)
print(diez)

# Tipado dinámico: las variables pueden almacenar diferentes tipos de datos en diferentes momentos
# Se recomienda no hacer esto, es mejor almacenar un mismo tipo de dato durante todo el programa
valor = "Eduardo"
valor = 2
valor = 3.1
valor = True
print(valor)


# Conocer el tipo de dato: función type

valor = "Eduardo"
tipo = type(valor)
print(tipo)

valor = 2
tipo = type(valor)
print(tipo)

valor = 3.1
tipo = type(valor)
print(tipo)

valor = True
tipo = type(valor)
print(tipo)


# También se pueden ahorra una variable juntando funciones (refactor)
valor = "Eduardo"
print(type(valor))

valor = 2
print(type(valor))

valor = 3.1
print(type(valor))

valor = True
print(type(valor))

# GENERAR UN LISTADO A PARTIR DE UN STRING

# Método Split: divide el texto usando espacios
lenguajes = 'Python Ruby Java Rust C++ C'
print(lenguajes)

listado_lenguajes = lenguajes.split()  # espacios
print(listado_lenguajes)
print(type(listado_lenguajes))

# Método Split: divide el texto usando caracteres
lenguajes = 'Python//Rub//Jav//Rus//C+//C'
listado_lenguajes = lenguajes.split('//')  # backslash
print(listado_lenguajes)

lenguajes = 'Python, Rub, Jav, Rus, C+, C'
listado_lenguajes = lenguajes.split(', ')  # comas y espacio
print(listado_lenguajes)

lenguajes = 'Python,Rub,Jav,Rus,C+,C'
listado_lenguajes = lenguajes.split(',')  # comas sin espacio
print(listado_lenguajes)

# Split utilizando un númnero dado de coincidencias
lenguajes = 'Python, Rub, Jav, Rus, C+, C'
listado_lenguajes = lenguajes.split(', ', 2)  # comas y espacio
print(listado_lenguajes)


# GENERAR UN STRING A PARTIR DE UN LISTADO

# Unir elementos de una lista usando el método JOIN
lenguajes = ['Python', 'Ruby', 'Java', 'Rust']
print(lenguajes)

string_lenguajes = ' '.join(lenguajes)
print(string_lenguajes)
print(type(string_lenguajes))

string_lenguajes = '-'.join(lenguajes)
print(string_lenguajes)

string_lenguajes = ' - '.join(lenguajes)
print(string_lenguajes)

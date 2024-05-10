# Concatenar Stings
nombre = 'Eduardo Ismael'
apellido = 'García'

nombre_completo = nombre + apellido
print(nombre_completo)  # palabras pegadas

nombre_completo = nombre + ' ' + apellido
print(nombre_completo)  # palabras no pegadas

nombre_completo = 'Mr.' + nombre + ' ' + apellido + '.'
print(nombre_completo)

# Con %s
nombre_completo = 'Mr. %s %s.' % (nombre, apellido)
print(nombre_completo)

nombre_completo = 'Mr. %s %s %s.' % (nombre, apellido, 'Pérez')
print(nombre_completo)

# Con el método format y posición de valores
nombre_completo = 'Mr. {} {}.'.format(nombre, apellido)
print(nombre_completo)

nombre_completo = 'Mr. {} {} {}.'.format(nombre, apellido, 'Pérez')
print(nombre_completo)

# Con el método format y variables
nombre_completo = 'Mr. {nombre} {primer_apellido} {segundo_apellido}.'.format(
    nombre=nombre,
    primer_apellido=apellido,
    segundo_apellido='Pérez'
)
print(nombre_completo)

# Con f-strings utilizando interpolación
nombre_completo = f'Mr. {nombre} {apellido} {"Pérez"}'
print(nombre_completo)

nombre_completo = f'Mr. {nombre} {apellido} {1}'
print(nombre_completo)

nombre_completo = f'Mr. {nombre} {apellido} {1.14}'
print(nombre_completo)

nombre_completo = f'Mr. {nombre} {apellido} {True}'
print(nombre_completo)

nombre_completo = f'Mr. {nombre} {apellido} { 10 * 20 }'
print(nombre_completo)

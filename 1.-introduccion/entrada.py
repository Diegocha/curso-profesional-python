# Datos que entran por teclado

# Leer un string
# por defecto input da str
nombre_completo = input('Ingresa tu nombre completo: ')
print(nombre_completo)
print(type(nombre_completo))


# Leer un entero
edad = input('Ingresa tu edad: ')
edad = int(edad)


# Leer un entero: menos líneas de código (refactor)
edad = int(input('Ingresa tu edad: '))


# Leer un flotante
altura = float(input('Ingresa tu altura: '))


# Leer un string y comparar
autorizacion = input('¿Autorizas el programa? (si/no): ') == 'si'


# Mostrando en consola
print(nombre_completo)
print(edad)
print(altura)
print(autorizacion)

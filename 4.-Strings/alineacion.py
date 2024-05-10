# Se usan estos tres métodos, que no modifican al string inicial
# ljust -> Justificar a la Izquierda
# rjust -> Justificar a la Derecha
# center -> Centrar
# El número indica los caracteres que se añaden

mensaje = 'Hola mundo!'
mensajeL = mensaje.ljust(20)
mensajeC = mensaje.center(20)
mensajeR = mensaje.rjust(20)

print(mensaje)
print(mensajeL)
print(mensajeC)
print(mensajeR)

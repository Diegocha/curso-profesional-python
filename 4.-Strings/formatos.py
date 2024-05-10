mensaje = '   Curso profesional de Python, donde aprenderemos Python.   '

mensaje = mensaje.upper()  # Convierte a MAYÚSCULAS
print(mensaje)
print(mensaje.isupper())

mensaje = mensaje.lower()  # Convierte a minúsculas
print(mensaje)
print(mensaje.islower())
print(mensaje.isupper())

mensaje = mensaje.strip()  # Elimina espacios al inicio y al final
print(mensaje)

mensaje = mensaje.replace(' ', '-')  # Reemplaza espacios por -
print(mensaje)

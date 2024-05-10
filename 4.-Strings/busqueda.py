# Buscar un string dentro de otro string
titulo_curso = 'Curso profesional de Python'
contador = titulo_curso.count('Python')
print(contador)


titulo_curso = 'Curso profesional de Python, donde aprenderemos Python'
contador = titulo_curso.count('Python')
print(contador)

titulo_curso = 'Curso profesional de Python, donde aprenderemos Python'
contador = titulo_curso.count('a')
print(contador)

contador = titulo_curso.count('x')
print(contador)


# Decir si se encuentra o no el string
titulo_curso = 'Curso profesional de Python, donde aprenderemos Python'
print('Python' in titulo_curso)
print('python' in titulo_curso)
print('python' in titulo_curso.lower())
print('codigofacilito' not in titulo_curso.lower())


# startswith: Si el string inicia con
print(titulo_curso.startswith('Python'))


# endswith: Si el string termina con
print(titulo_curso.endswith('Python'))

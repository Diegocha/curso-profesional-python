lista = ['String', 10, 15.6, True]
print(lista)

lista_enteros = [8, 5, 90, 1, 5, 44, 132, 600, 3, 4, 5]
print(lista_enteros)

lista_booleanos = [True, True, (2 < 10), (4 > 3 and 10 != 11)]
print(lista_booleanos)


# Indices en una lista empiezan en 0 (izq a der)
lista_cursos = ['Python', 'Flask', 'Ruby', 'Java']

primer_curso = lista_cursos[0]
print(primer_curso)

segundo_curso = lista_cursos[1]
print(segundo_curso)


# Indices negativos empiezan en -1 (der a izq)
ultimo_curso = lista_cursos[-1]
print(ultimo_curso)

penultimo_curso = lista_cursos[-2]
print(penultimo_curso)


# Actualizar elmentos dentro de la lista
lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java']
print(lista_cursos)

lista_cursos[4] = 'Rust'
print(lista_cursos)


# Generar una sublista:
# [start:final]  -> elementos desde start hasta (final-1)
# [start:]  -> elementos desde start hasta el final
# [:end]  -> elementos desde el inicio hasta (end-1)
# [start:end:skip]  -> Genera la lista saltando
# [::-1]  -> Genera la lista invertida
# [:]  -> Sublista con todos los elementos de la lista inicial

lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
print(lista_cursos)

sub_lista = lista_cursos[0:3]  # No incluye el indice 3
print(sub_lista)

sub_lista = lista_cursos[1:4]  # No incluye el indice 4
print(sub_lista)

sub_lista = lista_cursos[1:100]  # No hay error
print(sub_lista)

sub_lista = lista_cursos[3:]  # No hay error, últimos elementos
print(sub_lista)

sub_lista = lista_cursos[:3]  # No hay error, primeros elementos
print(sub_lista)

sub_lista = lista_cursos[1:5:2]
print(sub_lista)

sub_lista = lista_cursos[:]
print(sub_lista)

sub_lista = lista_cursos[::-1]
print(sub_lista)


# Modificar lista: append adiciona elemento al final
lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
print(lista_cursos)

lista_cursos.append('MongoDB')
print(lista_cursos)

lista_cursos.append('C#')
print(lista_cursos)

lista_cursos.append('JavaScript')
print(lista_cursos)

print(len(lista_cursos))


# Modificar lista: insert adiciona elemento en un índice dado
lista_cursos.insert(1, 'Rails')
print(lista_cursos)
print(len(lista_cursos))

lista_cursos.insert(0, 'PyGame')
print(lista_cursos)
print(len(lista_cursos))


# Modificar lista: extend extiende la lista 1 sin afectar la lista 2
lista_cursos_2 = ['C', 'C++', 'Docker']
lista_cursos.extend(lista_cursos_2)
print(lista_cursos)
print(lista_cursos_2)


# Modificar lista: delete borra elementos dados
lista_cursos.remove('MongoDB')
print(lista_cursos)

# Modificar lista: del elimina un elemento en un índice
del lista_cursos[0]
print(lista_cursos)


# Modificar lista: clear deja la lista vacía
lista_cursos.clear()
print(lista_cursos)
print(len(lista_cursos))


# Operaciones con listas: sort ordena ascendentemente
lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]
lista.sort()
print(lista)

# Operaciones con listas: sort con reverse ordena descendentemente
lista.sort(reverse=True)
print(lista)

# Operaciones con listas: máx y mín
print(lista[0])   # mín
print(lista[-1])  # máx

print(min(lista))  # mín
print(max(lista))  # max

# Operaciones con listas: in para buscar pertenencia
print(lista)
print(10 in lista)
print(5 in lista)

# Operaciones con listas: not in para buscar no pertenencia
print(lista)
print(11 not in lista)

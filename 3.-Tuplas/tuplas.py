# LAS TUPLAS SON INMUTABLES: no cambian elementos ni longitud

# Las tuplas se definen con paréntesis
tupla = ()
print(type(tupla))

# Las tuplas permiten diferentes tipos de datos
tupla = ('String', 10, 15.4, True, [1, 2, 3], (4, 5, 6))
print(tupla)

# Las tuplas manejan índices
tupla = ('String', 10, 15.4, True, [1, 2, 3], (4, 5, 6))
#           0       1    2     3       4          5
print(tupla[0])
print(tupla[-1])  # esta es otra tupla

cursos = ('Python', 'Flask', 'Django', 'Rails', 'MongoDB')
#           0           1       2          3        4
primer_curso = cursos[0]
print(primer_curso)

ultimo_curso = cursos[-1]
print(ultimo_curso)

sub_tupla = cursos[:]
print(sub_tupla)

sub_tupla = cursos[0:3]
print(sub_tupla)

sub_tupla = cursos[:3]
print(sub_tupla)

# Ejercicio

'''
Crea una lista "asignaturas" con los textos "matematicas", "fisica", "historia"
Crea una lista "notas" con los valores 9, 9, 8
Crea una serie con la lista "notas" como valores, y la lista "asignaturas" como índices
Crea la variable "nota_fisica" con la nota de la asignatura de "fisica"
Mediante el método "print" muestra la frase "La nota de fisica es un ...." (sustituir ... por la nota de fisica)
'''

import pandas as pd
asignaturas = ['matematicas', 'fisica', 'historia']
print(asignaturas)

print()

notas = [9, 9, 8]
print(notas)

print()

serie = pd.Series(data=notas, index=asignaturas)
print(serie)

print()

nota_fisica = serie['fisica']
print(nota_fisica)

print()

print("La nota de fisica es un {}".format(nota_fisica))
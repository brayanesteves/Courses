# Ejercicio

'''
Dada la siguiente lista de palabras,
    lista = ["manzana", "platano", "melocoton", "pera", "manzana", "pera", "limon", "platano", "naranja"]
crea una nueva lista "lista_sin_duplicados" eliminando las palabras repetidas
Pista: Utilizar conjuntos
'''
lista = ["manzana", "platano", "melocoton", "pera", "manzana", "pera", "limon", "platano", "naranja"]
print(lista)

conjunto = set(lista)
print(conjunto)
lista_sin_duplicados = []
for elemento in conjunto:
    lista_sin_duplicados.append(elemento)
print(lista_sin_duplicados)
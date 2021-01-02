# Ejercicio

'''
Dada la siguiente lista de valores
    lista = [1, -1, 4, -15, 9, 7, 6, -3, 2, -20]
Crear un función "positivo" que pasando como paramtro un número, lo devuelve tal cual si es positivo,
    o devuelve nada si el número es negativo
Crear una nueva lista "lista2", que meduante "filter", contenga solo los números positivos de la lista inicial
'''
lista = [1, -1, 4, -15, 9, 7, 6, -3, 2, -20]
print(lista)

def positivo(numero):
    if (numero >= 0):
        return numero
print(positivo(-5))
print(positivo(6))

lista2 = list(filter(positivo, lista))
print(lista2)
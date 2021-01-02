# Ejercicio

'''
Crear una función "dividir_entre_dos", que divide un número entre el número "2" y devuelve el resultado
Dada la siguiente lista = [20, 18, 8, 4, 10, 40, 6]
Crear una nueva lista "lista2" que mediante la función "map" aplique la función "dividir_entre_dos"
    a cada elemento de la lista
'''
def dividir_entre_dos(numero):
    resultado = numero / 2
    return resultado

print(dividir_entre_dos(10))
print(dividir_entre_dos(5))

lista = [20, 18, 8, 4, 10, 40, 6]

lista2 = list(map(dividir_entre_dos, lista))
print(lista2)

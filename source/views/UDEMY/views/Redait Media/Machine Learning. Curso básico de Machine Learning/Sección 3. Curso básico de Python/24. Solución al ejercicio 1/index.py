# Ejercicio

'''
Dada la siguiente frase
    frase = "Hola, este es un curso básico de Python"
Divide la frase en palabras y cuenta el número de palabras que contiene esa frase
Muestra el resultado mediante "print" de esta forma:
    El número de palabras es .....
'''
frase = "Hola, este es un curso básico de Python"
palabras = frase.split()
print(palabras)
numero = 0
for palabra in palabras:
    numero = numero + 1
print("El número de palabras es {}".format(numero))
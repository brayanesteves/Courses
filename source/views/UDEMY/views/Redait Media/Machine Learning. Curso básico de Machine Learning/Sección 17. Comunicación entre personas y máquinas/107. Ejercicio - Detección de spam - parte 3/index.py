# Procesamiento del lenaguaje natural
print("Procesamiento del lenguaje natural")

import nltk

mensajes = [line.rstrip() for line in open("smsspamcollection/SMSSpamCollection")]
print(mensajes[0])

print()

print(mensajes[1])

print()

print(len(mensajes))

for mensajes in enumerate(mensajes[:5]):
    print(mensajes)

import pandas as pd

mensajesdf = pd.read_csv("smsspamcollection/SMSSpamCollection", sep="\t", names=["etiqueta", "mensaje"])
print(mensajesdf.head())

print()

mensajesdf["longitud"] = mensajesdf["mensaje"].apply(len)
print(mensajesdf.head())

import matplotlib.pyplot as plt
import seaborn as sn

mensajesdf["longitud"].plot.hist(bins=100)
plt.show()
mensajesdf["longitud"].plot.hist(bins=200)
plt.show()
print(mensajesdf["longitud"].describe())

print()

print(mensajesdf[mensajesdf["longitud"] == 910]["mensaje"])

print()

print(mensajesdf[mensajesdf["longitud"] == 910]["mensaje"].iloc[0])

mensajesdf.hist(column="longitud", by="etiqueta", bins=100, figsize=(10, 5))
plt.show()

# Procesamiento de texto
print("Procesamiento de texto\n")

import string

cadena = 'Mensaje de ejemplo! Nota: Este mensaje tiene signo de puntuación'
print(cadena)

print()

print(string.punctuation)

print()

sinpuntuacion = [c for c in cadena if c not in string.punctuation]
sinpuntuacion = ''.join(sinpuntuacion)
print(sinpuntuacion)

from nltk.corpus import stopwords

print(stopwords.words("spanish"))

print()

palabras = sinpuntuacion.split()
print(palabras)

print()

cadena_limpia = [palabra for palabra in palabras if palabra.lower() not in stopwords.words("spanish")]
print(cadena_limpia)

def procesar_texto(cadena):
    sinpuntuacion = [c for c in cadena if c not in string.punctuation]
    sinpuntuacion = ''.join(sinpuntuacion)
    palabras = sinpuntuacion.split()
    cadena_limpia = [palabra for palabra in palabras if palabra.lower() not in stopwords.words("spanish")]
    return cadena_limpia

print()

cadena = 'Mensaje de ejemplo! Nota: Este mensaje tiene signo de puntuación'
resultado = procesar_texto(cadena)
print(resultado)

print()

print(mensajesdf.head())

print()

print(mensajesdf["mensaje"].head(5).apply(procesar_texto))

print()

from sklearn.feature_extraction.text import CountVectorizer

transformador = CountVectorizer(analyzer=procesar_texto).fit(mensajesdf["mensaje"])
print(transformador.vocabulary_)

print()

mensaje3 = mensajesdf["mensaje"][3]
print(mensaje3)

print()

mensaje3_transformado = transformador.transform([mensaje3])
print(mensaje3_transformado)

print()

print(transformador.get_feature_names()[4199])

print()

print(transformador.get_feature_names()[4799])

print()

print(transformador.get_feature_names()[9785])
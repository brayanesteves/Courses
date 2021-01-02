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
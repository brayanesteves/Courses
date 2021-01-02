# Pandas - Ficheros HTML
print("Pandas - Ficheros HTML\n")

import pandas as pd

pagina_web = 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_y_territorios_dependientes_por_poblaci%C3%B3n'
datos = pd.read_html(pagina_web)
print(datos)

print()

print(type(datos))

print()

print(datos[0])

print()

dataframe = datos[0]
print(dataframe.head(10))
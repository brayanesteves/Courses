# Estilos y colores
print("Estilos y colores\n")

import seaborn as sns
import matplotlib.pyplot as plt

propinas = sns.load_dataset('tips')
propinas.head()

sns.set_context('notebook', font_scale=1.2)
plt.figure(figsize=(8, 4))
sns.set_style('white')
sns.countplot(x='sex', data=propinas)
sns.despine(left=True, bottom=True)

sns.countplot(x='sex', data=propinas, palette='Set2')
sns.countplot(x='sex', data=propinas, palette='hus1')

colores = ["lightgreen", "blue"]
sns.countplot(x='sex', data=propinas, palette=colores)

colores = ["#73e470", "#adaae7"]
sns.countplot(x='sex', data=propinas, palette=colores)
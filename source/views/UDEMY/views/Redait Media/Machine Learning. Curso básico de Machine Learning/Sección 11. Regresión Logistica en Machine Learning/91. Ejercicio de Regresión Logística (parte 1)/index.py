# Ejemplo regresión logística
print("Ejemplo regresión logística\n")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

entrenamiento = pd.read_csv('train.csv')

entrenamiento.head()
entrenamiento.isnull()

sns.heatmap(entrenamiento.isnull())

sns.countplot(x='Survived', data=entrenamiento)
sns.countplot(x='Survived', data=entrenamiento, hue='Sex')

entrenamiento.columns

sns.countplot(x='Survived', data=entrenamiento, hue='Pclass')

sns.displot(entrenamiento['Age'].dropna(), kde=False, bins=30)

entrenamiento['Age'].plot.hist(bins=30)
entrenamiento['SibSp'].plot.hist(bins=30)

import cufflinks as cf

cf.go_offline()

entrenamiento['Fare'].iplot(kind='hist', bins=40)
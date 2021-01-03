# Gráficos de cuadrícula (grids): PaisGrid y FacetGrid
print("Gráficos de cuadrícula (grids): PairGrid y FacetGrid\n")

import seaborn as sns
import matplotlib.pyplot as plt

flores = sns.load_dataset('iris')
flores.head()
'''
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa
'''

sns.pairplot(flores)

graficos = sns.PairGrid(flores)
graficos.map(plt.scatter)

graficos = sns.PairGrid(flores)
graficos.map_diag(sns.distplot)

graficos = sns.PairGrid(flores)
graficos.map_diag(sns.distplot)
graficos.map_upper(plt.scatter)

graficos = sns.PairGrid(flores)
graficos.map_diag(sns.distplot)
graficos.map_upper(plt.scatter)
graficos.map_lower(sns.kdeplot)

# FacetGrid
print("\nFacetGrid\n")

propinas = sns.load_dataset('tips')
propinas.head(10)
'''
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
5       25.29  4.71    Male     No  Sun  Dinner     4
6        8.77  2.00    Male     No  Sun  Dinner     2
7       26.88  3.12    Male     No  Sun  Dinner     4
8       15.04  1.96    Male     No  Sun  Dinner     2
9       14.78  3.23    Male     No  Sun  Dinner     2
'''

propinas['time'].unique()
'''
['Dinner', 'Lunch']
Categories (2, object): ['Dinner', 'Lunch']
'''

propinas['sex'].unique()

propinas['smoker'].unique()

propinas['day'].unique()

graficos2 = sns.FacetGrid(data=propinas, col='time', row='smoker')
graficos2.map(sns.distplot, 'total_bill')

graficos2 = sns.FacetGrid(data=propinas, col='time', row='smoker')
graficos2.map(plt.scatter, 'total_bill', 'tip')
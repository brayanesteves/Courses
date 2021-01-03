# Gráficos de regresión (Regresión Plots)
prin("Gráficos de regresión (Regresión Plots)\n")

import seaborn as sns

propinas = sns.load_dataset('tips')
propinas.head()
'''
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
'''

sns.lmplot(x='total_bill', y='tip', data=propinas)
sns.lmplot(x='total_bill', y='tip', data=propinas, hue='sex')
sns.lmplot(x='total_bill', y='tip', data=propinas, hue='sex', markers=['o', 'x'])
sns.lmplot(x='total_bill', y='tip', data=propinas, hue='sex', markers=['o', 'v'])
sns.lmplot(x='total_bill', y='tip', data=propinas, hue='sex', markers=['o', 'v'], scatter_kws={'s':80})
sns.lmplot(x='total_bill', y='tip', data=propinas, hue='sex', markers=['o', 'v'], scatter_kws={'s':60})
sns.lmplot(x='total_bill', y='tip', data=propinas)
sns.lmplot(x='total_bill', y='tip', data=propinas, col='sex')
sns.lmplot(x='total_bill', y='tip', data=propinas, col='day')
sns.lmplot(x='total_bill', y='tip', data=propinas, col='day', row='sex')
sns.lmplot(x='total_bill', y='tip', data=propinas, col='day', hue='sex')
sns.lmplot(x='total_bill', y='tip', data=propinas, col='day', hue='smoker')
sns.lmplot(x='total_bill', y='tip', data=propinas)
sns.lmplot(x='total_bill', y='tip', data=propinas, aspect=0.8, size=10)
sns.lmplot(x='total_bill', y='tip', data=propinas, aspect=0.3, size=15)
sns.lmplot(x='total_bill', y='tip', data=propinas, aspect=0.8, size=10)
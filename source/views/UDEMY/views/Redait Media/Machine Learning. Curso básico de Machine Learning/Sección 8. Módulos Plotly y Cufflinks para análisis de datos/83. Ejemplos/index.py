# Plotly y Cufflinks - Visualizaciones interactivas
print("Plotly y Cufflinks - Visualizaciones interactivas\n")

import pandas as pd
import numpy as np

import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=True)

cf.go_offline()

#%matplotlib inline

dataframe = pd.DataFrame(np.random.randn(100, 4), columns=['a', 'b', 'c', 'd'])
print(dataframe)
'''
{'text/html': '        <script type="text/javascript">\n        window.PlotlyConfig = {MathJaxConfig: \'local\'};\n        if (window.MathJax) {MathJax.Hub.Config({SVG: {font: "STIX-Web"}});}\n        if (typeof require !== \'undefined\') {\n        require.undef("plotly");\n        requirejs.config({\n            paths: {\n                \'plotly\': [\'https://cdn.plot.ly/plotly-latest.min\']\n
   }\n        });\n        require([\'plotly\'], function(Plotly) {\n            window._Plotly = Plotly;\n        });\n        }\n     
   </script>\n        '}
           a         b         c         d
0  -0.405184  1.919221 -1.248765 -0.584002
1   1.050658 -0.227597  0.288766 -0.909553
2  -0.071926  0.257812  0.728575 -0.381936
3  -0.019239  2.702747 -0.604956  2.705322
4   0.340468  0.632549  2.742161 -0.455874
..       ...       ...       ...       ...
95  0.332779  0.460445 -0.230799  0.410318
96 -1.583265  0.303155 -1.033717  0.782295
97 -0.923872 -0.801203  0.772295  0.856741
98 -0.866327  0.515375 -1.737868 -0.701366
99  0.225490  0.108388 -0.237543 -1.823013

[100 rows x 4 columns]
'''

dataframe.plot()

dataframe.iplot()
dataframe.iplot(kind='scatter', x='a', y='b', mode='markers')
dataframe.iplot(kind='bar')
dataframe.sum().iplot(kind='bar')
dataframe.iplot(kind='box')
dataframe['a'].iplot(kind='hist', bins=30)
dataframe.iplot(kind='hist', bins=30)
dataframe[['a', 'b']].iplot(kind='spread')
dataframe.iplot(kind='bubble', x='a', y='b', size='c')
dataframe2 = pd.DataFrame({'a': [1, 2, 3, 4], 'b': [30, 40, 20, 10], 'c': [12, 16, 18, 15]})
print(dataframe2)
'''
'''
dataframe2.iplot(kind='surface')
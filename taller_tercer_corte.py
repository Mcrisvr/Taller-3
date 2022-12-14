# -*- coding: utf-8 -*-
"""Taller tercer corte

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1foNQ5whhmc3hfTkiYUoO6DoP5UMqhccn

#TALLER

Laura Hernández

Daniel Mateo Bernal

María Cristina Vidales
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as seaborn

df = pd.read_csv('datos.csv')

df

"""#Exploración inicial"""

df.head(10)

"""###Conclusión: Entre las 10 primeras, solo dos están cerca a una arteria, ninguna tiene piscina, solo una tiene una habitación y la más vieja tiene 107 años de construcción."""

df.tail(10)

"""###Conclusión: Entre las 10 últimas, ninguna está cerca a una arteria, ninguna tiene piscina, todas tienen más de una habitación y la más vieja tiene 81 años de construcción."""

len(df.columns)

print("Number of Rows:", len(df))

df.info()

"""###Conclusión: Todos los tipos de datos son números enteros y no tienen datos nulos."""

df.describe()

df.isna().sum()

df.duplicated().sum()

df.isnull()

df.drop_duplicates()

"""#Visualización de datos
###Visualización univariada
"""

from pandas.io.formats.style import plt
plt.hist(df["LotArea"])

"""Conclusión: la mayoría de viviendas tienen un área entre 0 y 50000."""

from pandas.io.formats.style import plt
plt.hist(df["OverallQual"])

"""Conclusión: La calidad general de las viviendas va aumentando hasta llegar al 5, a partir de ahí, la calidad general del inmueble comienza a disminuir.  

"""

from pandas.io.formats.style import plt
plt.hist(df["OverallCond"])

"""Conclusión: La cantidad de viviendas aumenta en menor medida aproximadamente entre 2 y 4 de la condición general del inmueble, entre 4 y 5 no presenta ninguna condición general de la vivienda. La mayoría de las viviendas tienen una condición general entre 5 y 6, y desde este intervalo la cantidad de viviendas empieza a disminuir respecto a la condición general del inmueble. """

from pandas.io.formats.style import plt
plt.hist(df["YearBuilt"])

"""Conclusión: La mayoría de las casas tienen 20 años de construidas.
 
"""

from pandas.io.formats.style import plt
plt.hist(df["YearRemodAdd"])

"""Conclusión: Aproximadamente la mayoría de las viviendas tienen entre 10 y 20 años de remodelación y la menor cantidad de viviendas tienen 40 años de remodelación. """

from pandas.io.formats.style import plt
plt.hist(df["ExterQual"])

"""Conclusión: La mayoría de las viviendad tienen una calidad de la fachada de 3."""

from pandas.io.formats.style import plt
plt.hist(df["ExterCond"])

"""Conclusión: La mayoría de las viviendas tienen una condición de fachada entre 3 y 3,5."""

from pandas.io.formats.style import plt
plt.hist(df["BedroomAbvGr"])

"""Conclusión: La cantidad de viviendas va aumentando entre 0 y 3 cantidad de habitaciones, ninguna vivienda tiene entre 3 y 4 cantidad de habitaciones, y desde 4 hasta aproximadamente 6 habitaciones, la cantidad de viviendas comienza a disminuir.  """

from pandas.io.formats.style import plt
plt.hist(df["GarageCars"])

"""Conclusión: La mayoría de viviendas tienen entre 2 y 2,5 garajes."""

from pandas.io.formats.style import plt
plt.hist(df["PoolArea"])

"""Conclusión: Ninguna casa tiene piscina. """

from pandas.io.formats.style import plt
plt.hist(df["SalePrice"])

"""Conclusión: La mayoría de las viviendas tienen un precio de entre 100000 y 200000, a partir de este valor, a medida que aumenta el precio la cantidad de viviendas disminuye."""

sns.barplot(data=df, x='Artery', y='SalePrice')

import seaborn as sns

sns.boxplot(data=df, x='Artery', y='SalePrice')

"""Conclusión: Podemos estimar que en efecto, vivir cerca a una arteria reduce el precio de la vivienda. Mientras que, vivir lejos a una arteria no aumenta el precio. 

A su vez, podemos deducir que, la mediana de vivir lejos de una arteria, es mayor que la de estar cerca a una.

## Visualización bivariada
"""

sns.scatterplot(df['LotArea'],df['SalePrice'])

"""Conclusión: El precio se concentra mayormente en las viviendas que tienen un área de entre 0 y 50000. """

sns.scatterplot(df['OverallQual'],df['SalePrice'])

"""Conclusión: a medida que aumenta calidad general del inmueble, aumenta el precio. """

sns.scatterplot(df['OverallCond'],df['SalePrice'])

"""Conclusión: Cuando la condición general del inmueble esta en 5, la vivienda presenta el precio mayor.   """

sns.scatterplot(df['YearBuilt'],df['SalePrice'])

"""Conclusión: El precio disminuye en menor intensidad a medida que aumentan los años de construcción de la vivienda.  """

sns.scatterplot(df['YearRemodAdd'],df['SalePrice'])

"""Conclusión: El precio disminuye en menor intensidad a medida que aumentan los años de remodelación de la vivienda."""

sns.scatterplot(df['ExterQual'],df['SalePrice'])

"""Conclusión: a medida que aumenta calidad de la fachada, aumenta el precio."""

sns.scatterplot(df['ExterCond'],df['SalePrice'])

"""Conclusión: Cuando la condición de la fachada del inmueble esta en 3, la vivienda presenta el precio mayor."""

sns.scatterplot(df['BedroomAbvGr'],df['SalePrice'])

"""Conclusión: Entre 0 y 2 habitaciones el precio va aumentando, el precio mayor de la vivienda se presenta cuando el inmueble tiene 4 habitaciones, y desde esa cantidad el precio empieza a disminuir. """

sns.scatterplot(df['GarageCars'],df['SalePrice'])

"""Conclusión: El precio del inmueble aumenta entre 0 y 3 garajes, y disminuye cuando la vivienda tiene 4 garajes. """

sns.scatterplot(df['PoolArea'],df['SalePrice'])

"""Conclusión: Como ninguna casa tiene Piscina, esta variable no afecta el precio.

###Análisis de correlación
"""

df.corr()

"""#Conclusión
## El precio tiene correlación positiva con área del inmueble, calidad de la fachada, condición de la fachada, número de garajes y área de la piscina; pero tiene una correlación positiva fuerte con la calidad general del inmueble.

## El precio tiene correlación negativa con la condición general del inmueble y correlación negativa fuerte con año de remodelación y año de construcción. 
"""

df.corr(method="spearman")

"""#Conclusión
A pesar del cambio de método de Pearson a Spearman, se obtienen los mismos resultados:

El precio tiene correlación positiva con área del inmueble, calidad de la fachada, condición de la fachada, número de garajes y área de la piscina; pero tiene una correlación positiva fuerte con la calidad general del inmueble.

El precio tiene correlación negativa con la condición general del inmueble y correlación negativa fuerte con año de remodelación y año de construcción.

# Modelamiento
"""

y=df['SalePrice']
X= sm.add_constant(df[['Artery','OverallQual','YearBuilt','BedroomAbvGr','ExterQual','GarageCars']])
model= sm.OLS(y,X)
reg=model.fit()
reg.summary()

"""#Conclusión
## La única variable significativa es el año de construcción, ya que, tiene P-valor es mayor a 0,05 y esta misma variable nos indica que el coeficiente estimado incrementa el precio de la vivienda en $23.7926

#Conclusiones generales
##El precio de una vivienda se ve afectado por diferentes variables, como la calidad general que tenga el inmueble o el estar cerca o lejos de una arteria.
"""
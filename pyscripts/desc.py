#Helen O'Shea 22/03/2018 3

#adapted from https://machinelearningmastery.com/understand-machine-learning-data-descriptive-statistics-python/
#https://pandas.pydata.org/pandas-docs/stable/visualization.html
#http://www.scipy-lectures.org/packages/scikit-learn/auto_examples/plot_iris_scatter.html


import pandas
url = "https://raw.githubusercontent.com/Osheah/project/master/data/iris.csv?token=AiEuthVKeloCkMeFSmPeZBQ6oCblwRnRks5avOiwwA%3D%3D"
names = ['sepalL', 'sepalW', 'petalL', 'petalW', 'name']
iris = pandas.read_csv(url, names=names)
peek = iris.head(10)
print(peek)
shape = iris.shape
print(shape)
types = iris.dtypes
print(types)
pandas.set_option('display.width', 100)
pandas.set_option('precision', 3)
description = iris.describe()
print(description)
correlations = iris.corr(method='pearson')
print(correlations)
skew = iris.skew()
print(skew)



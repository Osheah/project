#Helen O'Shea 22/03/2018 3

#adapted from https://machinelearningmastery.com/understand-machine-learning-data-descriptive-statistics-python/
import pandas
url = "https://raw.githubusercontent.com/Osheah/project/master/data/iris.csv?token=AiEuthVKeloCkMeFSmPeZBQ6oCblwRnRks5avOiwwA%3D%3D"
names = ['sepalL', 'sepalW', 'petalL', 'petalW', 'name']
data = pandas.read_csv(url, names=names)
peek = data.head(10)
print(peek)
shape = data.shape
print(shape)
types = data.dtypes
print(types)
pandas.set_option('display.width', 100)
pandas.set_option('precision', 3)
description = data.describe()
print(description)
correlations = data.corr(method='pearson')
print(correlations)
skew = data.skew()
print(skew)
import matplotlib

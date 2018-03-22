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

# Load the data
from sklearn.datasets import load_iris
iris = load_iris()

from matplotlib import pyplot as plt

# The indices of the features that we are plotting
x_index = 0
y_index = 1

# this formatter will label the colorbar with the correct target names
formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

plt.figure(figsize=(5, 4))
plt.scatter(iris.data[:, x_index], iris.data[:, y_index], c=iris.target)
plt.colorbar(ticks=[0, 1, 2], format=formatter)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index])

plt.tight_layout()
plt.show()


iris.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm")

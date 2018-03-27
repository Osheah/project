#Helen O'Shea 22/03/2018 3

#adapted from https://machinelearningmastery.com/understand-machine-learning-data-descriptive-statistics-python/
#https://pandas.pydata.org/pandas-docs/stable/visualization.html
#http://www.scipy-lectures.org/packages/scikit-learn/auto_examples/plot_iris_scatter.html
#https://rstudio-pubs-static.s3.amazonaws.com/229050_116b97bac814449586325ff405417419.html
#https://www.kaggle.com/danalexandru/simple-analysis-of-iris-dataset

import pandas
url = "https://raw.githubusercontent.com/Osheah/project/master/data/iris.csv?token=AiEuthVKeloCkMeFSmPeZBQ6oCblwRnRks5avOiwwA%3D%3D"
names = ['sepalL', 'sepalW', 'petalL', 'petalW', 'name']
iris = pandas.read_csv(url, names=names)
'''peek = iris.head(10)
print(peek)
shape = iris.shape
print(shape)'''
types = iris.dtypes
print(types)
pandas.set_option('display.width', 100)
pandas.set_option('precision', 3)
description = iris.describe()
print("the description of ", "\r\n", description)
correlations = iris.corr(method='pearson')
'''print("the pearson correlations are", "\r\n", correlations)
skew = iris.skew()
print("The skew is: ","\r\n", skew)'''
print("All measurments are in cm")
print("The maximum sepal length is  ", description['sepalL'][7], "cm" )
print("The maximum sepal width is  ", description['sepalW'][7], "cm" )
print("The maximum petal length is  ", description['petalL'][7], "cm" )
print("The maximum petal width is  ", description['petalW'][7], "cm" )
print("The minimum sepal length is  ", description['sepalL'][3], "cm" )
print("The minimum sepal width is  ", description['sepalW'][3], "cm" )
print("The minimum petal length is  ", description['petalL'][3], "cm" )
print("The minimum petal width is  ", description['petalL'][3], "cm" )
print("The mean sepal length is  ", round(description['sepalL'][1], 3), "cm" )
print("The mean sepal width is  ", round(description['sepalW'][1],3), "cm" )
print("The mean petal length is  ", round(description['petalL'][1], 3), "cm" )
print("The mean petal width is  ", round(description['petalL'][1], 3), "cm" )



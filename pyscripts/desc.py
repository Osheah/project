#Helen O'Shea 22/03/2018 3

#adapted from https://machinelearningmastery.com/understand-machine-learning-data-descriptive-statistics-python/
#https://pandas.pydata.org/pandas-docs/stable/visualization.html
#http://www.scipy-lectures.org/packages/scikit-learn/auto_examples/plot_iris_scatter.html
#https://rstudio-pubs-static.s3.amazonaws.com/229050_116b97bac814449586325ff405417419.html
#https://www.kaggle.com/danalexandru/simple-analysis-of-iris-dataset

import pandas as pd
url = "../data/iris.csv" # location of data 
names = ['sepalL', 'sepalW', 'petalL', 'petalW', 'name'] # add the names of the headings
iris = pd.read_csv(url, names=names) # imports the data from the local data folder  and gives it the headings listed in names
peek = iris.head(10) # looks at the headers and first 10 items
print(peek) # prints the headers and first 10 items
with pd.option_context('display.max_rows', None, 'display.max_columns', 6): # use pandas to print the full data 6 col wide - one for col id and 5 for dimensions
    print(iris) # print out the complete data set

shape = iris.shape # get an idea of the dimension of the data 150 samples 5 dimensions
print(shape)# print the shape 
iris.info # general information about the data
types = iris.dtypes # type of data 4 floats - the length and widths of petals and sepals and 1 object of iris species name 
print(types)#view the data types
'''
select the data by species name 
'''
iris_se = iris['name'] == 'Iris-setosa' # select the iris setosa data
print(iris[iris_se].head(50)) # print all of the setosa data
iris_vi = iris['name'] == 'Iris-virginica' # select  the iris virginica data
print(iris[iris_vi].head(50))# print all the virginica data
iris_ve = iris['name'] == 'Iris-versicolor' # select the iris versicolor data
print(iris[iris_ve].head(50)) # print all the versicolor data


''' get data description of the iris categories'''
# set table up
pd.set_option('display.width', 100) 
pd.set_option('precision', 3) # display stats to 3 dp
# Setosa description and saved results
desc_se = iris[iris_se].describe() # use pandas describe to calcualte descriptive statistics
print("\r\n", "The descriptive statistics of the Iris Setosa Data is listed below", "\r\n", desc_se)
desc_se.to_csv("../data/desc_se.csv", sep='\t') # save the table in /data/ as desc_se.csv
# Virginica description and saved results
desc_vi = iris[iris_vi].describe() # use pandas describe to calcualte descriptive statistics
print("\r\n", "The descriptive statistics of the Iris Virginica Data is listed below", "\r\n", desc_vi)
desc_vi.to_csv("../data/desc_vi.csv", sep='\t') # save the table in /data/ as desc_vi.csv
#Versicolor description and saved results
desc_ve = iris[iris_ve].describe() # use pandas describe to calcualte descriptive statistics
print("\r\n", "The descriptive statistics of the Iris Versicolor Data is listed below", "\r\n", desc_ve)
desc_ve.to_csv("../data/desc_ve.csv", sep='\t') # save the table in /data/ as desc_ve.csv
description = iris.describe()
print ("\r\n", "The descriptive statistics of the Iris Data is listed below", "\r\n", description)
description.to_csv("../data/description.csv", sep='\t') # save the table in /data/ as descriptioncla.csv

'''
correlations = iris.corr(method='pearson')
print("the pearson correlations are", "\r\n", correlations)
skew = iris.skew()
print("The skew is: ","\r\n", skew)

dont really need this so delete it
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
'''


#Helen O'Shea 22/03/2018 
#code adapted from https://machinelearningmastery.com/understand-machine-learning-data-descriptive-statistics-python/
#https://pandas.pydata.org/pandas-docs/stable/visualization.html
#http://www.scipy-lectures.org/packages/scikit-learn/auto_examples/plot_iris_scatter.html
#https://www.kaggle.com/benhamner/python-data-visualizations

# Import the packages
import pandas as pd # use pandas to import the csv 
url = "../data/iris.csv" # location of data 
names = ['sepalL', 'sepalW', 'petalL', 'petalW', 'name'] # add the names of the headings
iris = pd.read_csv(url, names=names) # imports the data from the local data folder  and gives it the headings listed in names
peek = iris.head(10) # looks at the headers and first 10 items
print(peek) # prints the headers and first 10 items to check data imported correctly.
with pd.option_context('display.max_rows', None, 'display.max_columns', 6): # use pandas to print the full data 6 col wide - one for col id and 5 for dimensions
#print(iris) # print out the complete data set
shape = iris.shape # get an idea of the dimension of the data 150 samples 5 dimensions
print(shape)# print the shape 
iris.info # general information about the data
types = iris.dtypes # type of data 4 floats - the length and widths of petals and sepals and 1 object of iris species name 
print(types)#view the data types

'''
select the data by species name - group and split the data by name 
'''

setosa=iris[(iris['name'] == 'Iris-setosa')] # select the iris setosa data only
print(setosa.head(50)) # print all of the setosa data as a check 
versicolor=iris[(iris['name'] == 'Iris-versicolor')] # select  the iris versicolor data only 
print(versicolor.head(50)) # print all the versicolor data as a check
virginica=iris[(iris['name'] == 'Iris-virginica')] # select the iris virginica data only as a check
print(versicolor.head(50)) # print all the virginica data only as a check


'''look at the ratios of length/width'''
#---------setosa----------------------
#sepal 
s_s_ratio=setosa['sepalL']/setosa['sepalW'] 
print(s_s_ratio, "/n")
s_s_desc = s_s_ratio.describe()
print("the setosa sepal ratio descriptions are ", "\r\n", s_s_desc)
s_s_desc.to_csv("../data/s_s_desc.csv", sep='\t') # save the file to data folder
#petal
s_p_ratio=setosa['petalL']/setosa['petalW']
print(s_p_ratio, "/n")
s_p_desc = s_p_ratio.describe()
print("the setosa petal ratio descriptions are ", "\r\n", s_p_desc)
s_p_desc.to_csv("../data/s_p_desc.csv", sep='\t')

#---------versicolor----------------------
#sepal
ve_s_ratio=versicolor['sepalL']/versicolor['sepalW']
print(ve_s_ratio, "/n")
ve_s_desc = ve_s_ratio.describe()
print("the versicolor sepal ratio descriptions are", "\r\n", ve_s_desc)
ve_s_desc.to_csv("../data/ve_s_desc.csv", sep='\t') # save the file to data folder
#petal
ve_p_ratio=versicolor['petalL']/versicolor['petalW']
print(ve_p_ratio, "/n")
ve_p_desc = ve_p_ratio.describe()
print("the versicolor petal ratio descriptions are ", "\r\n", ve_p_desc)
ve_p_desc.to_csv("../data/ve_p_desc.csv", sep='\t')

#---------virginica----------------------
#sepal
vi_s_ratio=virginica['sepalL']/virginica['sepalW']
print(vi_s_ratio, "/n")
vi_s_desc = vi_s_ratio.describe()
print("the virginica sepal ratio descriptions are ", "\r\n", vi_s_desc)
vi_s_desc.to_csv("../data/vi_s_desc.csv", sep='\t') # save the file to data folder
#petal
vi_p_ratio=virginica['petalL']/virginica['petalW']
print(vi_p_ratio, "/n")
vi_p_desc = vi_p_ratio.describe()
print("the virginica petal ratio descriptions are", "\r\n", vi_p_desc)
vi_p_desc.to_csv("../data/vi_p_desc.csv", sep='\t')

''' get data description of the iris species'''

# set table up
pd.set_option('display.width', 100) 
pd.set_option('precision', 3) # display stats to 3 dp

# Setosa description and saved results
desc_se = setosa.describe() # use pandas describe to calcualte descriptive statistics
print("\r\n", "The descriptive statistics of the Iris Setosa Data is listed below", "\r\n", desc_se)
desc_se.to_csv("../data/desc_se.csv", sep='\t') # save the table in /data/ as desc_se.csv

# Virginica description and saved results
desc_vi = virginica.describe() # use pandas describe to calcualte descriptive statistics
print("\r\n", "The descriptive statistics of the Iris Virginica Data is listed below", "\r\n", desc_vi)
desc_vi.to_csv("../data/desc_vi.csv", sep='\t') # save the table in /data/ as desc_vi.csv

#Versicolor description and saved results
desc_ve = versicolor.describe() # use pandas describe to calcualte descriptive statistics
print("\r\n", "The descriptive statistics of the Iris Versicolor Data is listed below", "\r\n", desc_ve)
desc_ve.to_csv("../data/desc_ve.csv", sep='\t') # save the table in /data/ as desc_ve.csv

#describe all the iris data
description = iris.describe()
print ("\r\n", "The descriptive statistics of the Iris Data is listed below", "\r\n", description)
description.to_csv("../data/description.csv", sep='\t') # save the table in /data/ as descriptioncla.csv






# Load libraries
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# Load iris data
url = "../data/iris.csv" # location of data 
names = ['sepalL', 'sepalW', 'petalL', 'petalW', 'name'] # add the names of the headings
iris = pd.read_csv(url, names=names) # imports the data from the local data folder  and gives it the headings listed in names
# test if iris data is differs from a normal distribution  - one tailed or two tailed?
iris.groupby("name")["sepalL"].describe()
setosa=iris[(iris['name'] == 'Iris-setosa')]
versicolor=iris[(iris['name'] == 'Iris-versicolor')]
virginica=iris[(iris['name'] == 'Iris-virginica')]
#print("The t-test for a relationship between Setosa and Versicolor Sepal Widths is:", stats.ttest_ind(setosa['sepalW'], versicolor['sepalW']))
#Ttest_indResult(statistic=9.2827725555581111, pvalue=4.3622390160102143e-15) p<0.05 so signifant there for reject null hypothesis H0 for HA that the populations are different. 

print("The mean of the Setosa Sepal Width is ",round(np.mean(setosa['sepalW']),3))
print("The standard deviation of the Setosa Sepal Width is ", round(np.std(setosa['sepalW']),3))

print("The mean of the versicolor Sepal Width is ",round(np.mean(versicolor['sepalW']),3))
print("The standard deviation of the versicolor Sepal Width is ", round(np.std(versicolor['sepalW']),3))

print("The t test between the setosa and versicolor sepal widths is ", stats.ttest_ind(setosa['sepalW'], versicolor['sepalW']))
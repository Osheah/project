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
'''
print("The mean of the Setosa Sepal Width is ",round(np.mean(setosa['sepalW']),3))
print("The standard deviation of the Setosa Sepal Width is ", round(np.std(setosa['sepalW']),3))

print("The mean of the versicolor Sepal Width is ",round(np.mean(versicolor['sepalW']),3))
print("The standard deviation of the versicolor Sepal Width is ", round(np.std(versicolor['sepalW']),3))

print("The t test between the setosa and versicolor sepal widths is ", stats.ttest_ind(setosa['sepalW'], versicolor['sepalW']))

print("The t-test between the sepal lengths of the Setosa and Versicolor is ", stats.ttest_ind(setosa['sepalL'], versicolor['sepalL'], equal_var=False))
'''
#----- Welch t test---------------
# define welch t test to get deg of freedom and p
#code taken from https://pythonfordatascience.org/welch-t-test-python-pandas/
def welch_ttest(x, y): 
    ## Welch-Satterthwaite Degrees of Freedom ##
    dof = (x.var()/x.size + y.var()/y.size)**2 / ((x.var()/x.size)**2 / (x.size-1) + (y.var()/y.size)**2 / (y.size-1))
   
    t, p = stats.ttest_ind(x, y, equal_var = False)
    
    print("\n",
          f"Welch's t-test= {t:.4f}", ", ",
          f"p-value = {p:.4f}", ", ",
          f"Welch-Satterthwaite Degrees of Freedom= {dof:.4f}")
#call the function
'''
print(welch_ttest(setosa['sepalL'], versicolor['sepalL']))

print("The t-test between the sepal lengths of the Setosa and Virginica is ", stats.ttest_ind(setosa['sepalL'], virginica['sepalL'], equal_var=False))
print(welch_ttest(setosa['sepalL'], virginica['sepalL']))
print("The Levene test for Sepal Lengths of versicolor and virginica is ", stats.levene(versicolor['sepalL'], virginica['sepalL']))

print("The t test between the petal widths of Versicolor and Virginica is ", stats.ttest_ind(versicolor['petalW'], virginica['petalW'], equal_var= False))
print(welch_ttest(versicolor['petalW'], virginica['petalW']))
print(stats.ttest_ind(setosa['petalL'], versicolor['petalL'], equal_var= False))
print(welch_ttest(setosa['petalL'], versicolor['petalL']))'''

print("The t-test between the Setosa and Virginica petal length is ", stats.ttest_ind(setosa['petalL'], virginica['petalL'], equal_var=False))
print(welch_ttest(setosa['petalL'], virginica['petalL']))

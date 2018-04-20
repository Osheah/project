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

# test the setosa petal widths with the outliers removed
# how to remove outliers
# how to identify outliers
#adapted from http://colingorrie.github.io/outlier-detection.html
#Outlier detection

def outliers_iqr(ys):
    quartile_1, quartile_3 = np.percentile(ys, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * 1.5)
    upper_bound = quartile_3 + (iqr * 1.5)
    return np.where((ys > upper_bound) | (ys < lower_bound))

print('The outliers as identifed by iqr are:' , '\n\r', outliers_iqr(setosa['petalW']))
print(setosa['petalW'][23])
print(setosa['petalW'][43])
#print(setosa)

#z score petal width of 0.6 looks enough to modify as 0.6 is much different from the other scores replace 0.6 with mean of petal width and check for normal distribution. 
#get mean petal widths for setosa
print(np.average(setosa['petalW']))
# change value 
#osetosa = setosa['petalW'].replace([0.5],2.44)
osetosa=(setosa['petalW']).replace([setosa['petalW'][23], setosa['petalW'][43]],.244)
plt.hist((setosa['petalW']).replace([setosa['petalW'][23], setosa['petalW'][43]],.244))
plt.show()
#looks normalish
# test for normality
print("The Shapiro Wilk test for the Setosa Petal Width with iqr outliers replaced by means is ", stats.shapiro(osetosa))


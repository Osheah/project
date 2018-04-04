#Helen O'Shea 22/03/2018 
# code adapted from https://pythonfordatascience.org/independent-t-test-python/

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


#---------Sepals---------------------

#---------Sepal Widths---------------
#-- Setosa vs Versicolor-------------
#test assumptions
# test if data satisfies assumptions for t test e.g. normal distribution and equal variance for categorial iv = names and continous dv = lengths/widths

#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the setosa sepal widths is the same as the mean of the versicolor sepal widths coming from the same population
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the setosa sepal widths is different from the mean of the versicolor sepal widths as the come from different populations
print("The Levene test for Sepal Widths of Setosa and Versicolor is ", stats.levene(setosa['sepalW'], versicolor['sepalW']))
#
# test is 

#check if sepal widths look normally distributed
setosa['sepalW'].plot(kind="hist", title="Setosa Sepal Width")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/setosasepalW.jpg')
plt.show()
versicolor['sepalW'].plot(kind="hist", title= "Versicolor Sepal Width", color="green")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/versicolorsepalW.jpg')
plt.show()

# histograms look to be normal distribution
# use q-q plot to see if data follows the red line. 
stats.probplot(setosa['sepalW'], dist="norm", plot= plt)
plt.title("Setosa Sepal Width Q-Q Plot")
plt.savefig("../graphs/setosaSW_qqplot.jpg")
plt.show()
# data looks okay in setosa

stats.probplot(versicolor['sepalW'], dist="norm", plot= plt)
plt.title("Versicolor Sepal Width Q-Q Plot")
plt.savefig("../graphs/versicolorSW_qqplot.jpg")
plt.show()
#data looks ok in versicolor

# test setosa for normality with Shapiro-Wilk test
print("The Shapiro Wilk test for normal distribution for the Setosa Sepal Widths is ",stats.shapiro(setosa['sepalW']))
#  

# test versicolor for normality with Shapiro-Wilk test
print("The Shapiro Wilk test for normal distribution for the Versicolor Sepal Widths is ", stats.shapiro(versicolor['sepalW']))
# 

#do t test
print("The t test between the setosa and versicolor sepal widths is ", stats.ttest_ind(setosa['sepalW'], versicolor['sepalW']))

# 

print("The mean of the Setosa Sepal Width is ",round(np.mean(setosa['sepalW']),3))
print("The standard deviation of the Setosa Sepal Width is ", round(np.std(setosa['sepalW']),3))
print("The mean of the versicolor Sepal Width is ",round(np.mean(versicolor['sepalW']),3))
print("The standard deviation of the versicolor Sepal Width is ", round(np.std(versicolor['sepalW']),3))

#Results Setosa sepal widths against Versicolor Sepal widths
#This tested if there is a significant difference in sepal widths between the Iris setosa and Iris versicolor. The Iris setosa’s average sepal width (M= , SD= ) is wider and has greater variation than Iris-versicolor (M=, SD= ). Levene’s test for homogeneity of variances indicated equality of variance (F= , p=); therefore an Independent t-test was used. Results showed a significant difference in sepal widths between Iris-setosa and Iris-versicolor (t(98)=, p=).

# now compare setosa sepal widths to virginica widths 

# #-- Setosa vs Virginica-------------
# test assumptions

#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the setosa sepal widths is the same as the mean of the virginica sepal widths coming from the same population
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the setosa sepal widths is different from the mean of the virginica sepal widths as the come from different populations

print("The Levene test for Sepal Widths of setosa and virginica is ", stats.levene(setosa['sepalW'], virginica['sepalW']))
#
#

#check if sepal width look normally distributed - setosa done already
virginica['sepalW'].plot(kind="hist", title= "Virginica Sepal Width", color="red")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/virginicasepalW.jpg')
plt.show()
# histograms look to be normal distribution

# use q-q plot to see if data follows the red line. setosa done already
stats.probplot(virginica['sepalW'], dist="norm", plot= plt)
plt.title("Virginica Sepal Width Q-Q Plot")
plt.savefig("../graphs/virginicaSW_qqplot.jpg")
plt.show()
#data looks ok in virginica

# test virginica for normality with Shapiro-Wilk test. setosa done already
print("The Shapiro Wilk test of Virginica Sepal Widths is ", stats.shapiro(virginica['sepalW']))
# 

#do t test
print("The t test between the sepal widths of Setosa and Virginica is ", stats.ttest_ind(setosa['sepalW'], virginica['sepalW']))
# 
print("The mean of the Setosa Sepal Width is ",round(np.mean(setosa['sepalW']),3))
print("The standard deviation of the Setosa Sepal Width is ", round(np.std(setosa['sepalW']),3))
print("The mean of the Virginica Sepal Width is ",round(np.mean(virginica['sepalW']),3))
print("The standard deviation of the Virginica Sepal Width is ", round(np.std(virginica['sepalW']),3))

#This tested if there is a significant difference in sepal widths between the Iris setosa and Iris virginica. The Iris setosa’s average sepal width (M= , SD= ) is wider and has greater variation than Iris-virginica (M= , SD=). Levene’s test for homogeneity of variances indicated equality of variance (F= , p=); therefore an Independent t-test was used. Results showed a significant difference in sepal widths between Iris-setosa and Iris-virginica (t(98)=, p=).

#--Versicolor vs Virginica-------------
# compare virginica to versicolor sepal widths

#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the versicolor sepal width is the same as the mean of the virginica sepal width coming from the same population
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the versicolor  sepal widths is different from the mean of the virginica sepal widths as the come from different populations

print("The Levene test for Sepal Widths of versicolor and virginica is ", stats.levene(versicolor['sepalW'], virginica['sepalW']))
#
# test not significant as p>0.05
#other tests done already
#do t test
print("The t test between the sepal widths of Versicolor and Virginica is ", stats.ttest_ind(versicolor['sepalW'], virginica['sepalW']))
#
print("The mean of the Versicolor Sepal Width is ",round(np.mean(versicolor['sepalW']),3))
print("The standard deviation of the Versicolor Sepal Width is ", round(np.std(versicolor['sepalW']),3))
print("The mean of the Virginica Sepal Width is ",round(np.mean(virginica['sepalW']),3))
print("The standard deviation of the Virginica Sepal Width is ", round(np.std(virginica['sepalW']),3))

#This tested if there is a significant difference in sepal widths between the Iris setosa and Iris virginica. The Iris setosa’s average sepal width (M= , SD= ) is wider and has greater variation than Iris-virginica (M= , SD=). Levene’s test for homogeneity of variances indicated equality of variance (F= , p=); therefore an Independent t-test was used. Results showed a significant difference in sepal widths between Iris-setosa and Iris-virginica (t(98)=, p=).



# do the same for sepal lengths

##------sepal lengths-----------
#-- Setosa vs Versicolor--------
# 
# test assumptions

#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the setosa sepal lengths the same as the mean of the versicolor sepal lengths coming from the same population
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the setosa sepal lengths is different from the mean of the versicolor sepal lengths as the come from different populations

print("The Levene test for sepal lengths between the Setosa and Versicolor is ", stats.levene(setosa['sepalL'], versicolor['sepalL']))
#
# test not significant as p>0.05

#check if sepal widths look normally distributed
setosa['sepalL'].plot(kind="hist", title="Setosa Sepal Length")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/setosasepalL.jpg')
plt.show()
versicolor['sepalL'].plot(kind="hist", title= "Versicolor Sepal Length", color="green")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/versicolorsepalL.jpg')
plt.show()
# histograms look to be normal distribution

# use q-q plot to see if data follows the red line. 
stats.probplot(setosa['sepalL'], dist="norm", plot= plt)
plt.title("Setosa Sepal Length Q-Q Plot")
plt.savefig("../graphs/setosaSL_qqplot.jpg")
plt.show()
# data looks okay in setosa

stats.probplot(versicolor['sepalL'], dist="norm", plot= plt)
plt.title("Versicolor Sepal Length Q-Q Plot")
plt.savefig("../graphs/versicolorSL_qqplot.jpg")
plt.show()
#data looks ok in versicolor

# test setosa for normality with Shapiro-Wilk test
print("The Shapiro Wilk test for the sepal lengths of the Setosa is", stats.shapiro(setosa['sepalL']))
# 

# test versicolor for normality with Shapiro-Wilk test
print("The Shapiro Wilk test for the sepal lengths of the Versicolor is ", stats.shapiro(versicolor['sepalL']))
#  
print("The mean of the Setosa Sepal length is ",round(np.mean(setosa['sepalL']),3))
print("The standard deviation of the Setosa Sepal length is ", round(np.std(setosa['sepalL']),3))
print("The mean of the versicolor Sepal Length is ",round(np.mean(versicolor['sepalL']),3))
print("The standard deviation of the versicolor Sepal Length is ", round(np.std(versicolor['sepalL']),3))

#do t test
print("The t-test between the sepal lengths of the Setosa and Versicolor is ", stats.ttest_ind(setosa['sepalL'], versicolor['sepalL']))
# 
#  
#This tested if there is a significant difference in sepal lengths between the Iris setosa and Iris versicolor. The Iris setosa’s average sepal length (M= , SD=) is smaller and has less variation than Iris-versicolor (M= , SD=). Levene’s test for homogeneity of variances indicated equality of variance (F=, p=); therefore an Independent t-test was used. Results showed a significant difference in sepal widths between Iris-setosa and Iris-versicolor (t(98)=, p=). 

# now compare setosa widths to virginica widths 
#-- Setosa vs Virginica-------------
# # perform t test
# test if data satisfies assumptions for t test e.g. normal distribution and equal variance for categorial iv = names and continous dv = lengths/widths

#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the setosa sepal lengths is the same as the mean of the virginica sepal lengths coming from the same population
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the setosa sepal lengths is different from the mean of the virginica sepal lengths as the come from different populations
print("The levene test for between the Setosa and Virginca sepal lengths is ", stats.levene(setosa['sepalL'], virginica['sepalL']))
#
# test not significant as p>0.05

#check if sepal width look normally distributed - setosa done already
virginica['sepalL'].plot(kind="hist", title= "Virginica Sepal Length", color="red")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/virginicasepalL.jpg')
plt.show()
# histograms look to be normal distribution

# use q-q plot to see if data follows the red line. setosa done already
stats.probplot(virginica['sepalL'], dist="norm", plot= plt)
plt.title("Virginica Sepal Length Q-Q Plot")
plt.savefig("../graphs/virginicaSL_qqplot.jpg")
plt.show()
#data looks ok in virginica

# test virginica for normality with Shapiro-Wilk test. setosa done already
print("The Shapiro Wilks test on the Virginia sepal lengths is ", stats.shapiro(virginica['sepalL']))
# 

#do t test
print("The t-test between the Setosa and Virginica Sepal Lengths is ", stats.ttest_ind(setosa['sepalL'], virginica['sepalL']))
#  

print("The mean of the Setosa Sepal Length is ",round(np.mean(setosa['sepalL']),3))
print("The standard deviation of the Setosa Sepal Length is ", round(np.std(setosa['sepalL']),3))
print("The mean of the Virginica Sepal Length is ",round(np.mean(virginica['sepalL']),3))
print("The standard deviation of the Virginica Sepal Length is ", round(np.std(virginica['sepalL']),3))

#This tested if there is a significant difference in sepal widths between the Iris setosa and Iris versicolor. The Iris setosa’s average sepal width (M= , SD= ) is wider and has greater variation than Iris-virginica (M= , SD=). Levene’s test for homogeneity of variances indicated equality of variance (F= , p=); therefore an Independent t-test was used. Results showed a significant difference in sepal widths between Iris-setosa and Iris-versicolor (t(98)=, p=).

# compare virginica to versicolor
#-- Versicolor vs Virginica-------------
#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the versicolor sepal widths is the same as the mean of the virginica sepal lengths  coming from the same population
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the versicolor  sepal lengths is different from the mean of the virginica sepal lengths as the come from different populations

print("The Levene test for Sepal Lengths of versicolor and virginica is ", stats.levene(versicolor['sepalL'], virginica['sepalW']))
#
# test not significant as p>0.05
#other tests done already
#do t test
print("The t test between the sepal lengths of Versicolor and Virginica is ", stats.ttest_ind(versicolor['sepalL'], virginica['sepalL']))
#
print("The mean of the Versicolor sepal length is ",round(np.mean(versicolor['sepalL']),3))
print("The standard deviation of the Versicolor Sepal length is ", round(np.std(versicolor['sepalL']),3))
print("The mean of the Virginica Sepal Length is ",round(np.mean(virginica['sepalL']),3))
print("The standard deviation of the Virginica Sepal length is ", round(np.std(virginica['sepalL']),3))

#This tested if there is a significant difference in sepal lengths between the Iris setosa and Iris virginica. The Iris setosa’s average sepal length (M= , SD= ) is wider and has greater variation than Iris-virginica (M= , SD=). Levene’s test for homogeneity of variances indicated equality of variance (F= , p=); therefore an Independent t-test was used. Results showed a significant difference in sepal widths between Iris-setosa and Iris-virginica (t(98)=, p=).

#-------------Petals------
#------------petal widths--

# perform t test
# test if data satisfies assumptions for t test e.g. normal distribution and equal variance for categorial iv = names and continous dv = lengths/widths

#-- Setosa vs Versicolor-------------
#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the petal widths is the same as the mean of the versicolor petal widths coming from the same population
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the setosa petal widths is different from the mean of the versicolor petal widths as the come from different populations
print("The Levene test between the Petal widths of the Setosa and Virginica is ", stats.levene(setosa['petalW'], versicolor['petalW']))
#
# test not significant as p>0.05

#check if sepal widths look normally distributed
setosa['petalW'].plot(kind="hist", title="Setosa Petal Width")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/setosapetalW.jpg')
plt.show()
versicolor['petalW'].plot(kind="hist", title= "Versicolor Petal Width", color="green")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/versicolorpetalW.jpg')
plt.show()
# histograms look to be normal distribution

# use q-q plot to see if data follows the red line. 
stats.probplot(setosa['petalW'], dist="norm", plot= plt)
plt.title("Setosa Petal Width Q-Q Plot")
plt.savefig("../graphs/setosaPW_qqplot.jpg")
plt.show()
# data looks okay in setosa

stats.probplot(versicolor['petalW'], dist="norm", plot= plt)
plt.title("Versicolor Petal Width Q-Q Plot")
plt.savefig("../graphs/versicolorPW_qqplot.jpg")
plt.show()
#data looks ok in versicolor

# test setosa for normality with Shapiro-Wilk test
print("The Shapiro Wilks test of the Setosa Petal Widths is ", stats.shapiro(setosa['petalW']))

# p>0.05 so not significant 

# test versicolor for normality with Shapiro-Wilk test
print("The Shapiro Wilks test of the Versicolor Petal Widths is ", stats.shapiro(versicolor['petalW']))

#  p>0.05 so not significant 

#do t test
print(stats.ttest_ind(setosa['petalW'], versicolor['petalW']))

# p<0.05 so signifant there for reject null hypothesis H0 for HA that the populations are different. 

print("The mean of the Setosa Petal Width is ",round(np.mean(setosa['petalW']),3))
print("The standard deviation of the Setosa Petal Width is ", round(np.std(setosa['petalW']),3))
print("The mean of the versicolor petal Width is ",round(np.mean(versicolor['petalW']),3))
print("The standard deviation of the Versicolor petal Width is ", round(np.std(versicolor['petalW']),3))

#This tested if there is a significant difference in petal widths between the Iris setosa and Iris versicolor. The Iris setosa’s average petal width (M= , SD= ) is wider and has greater variation than Iris-versicolor (M= , SD= ). Levene’s test for homogeneity of variances indicated equality of variance (F= , p=); therefore an Independent t-test was used. Results showed a significant difference in petal widths between Iris-setosa and Iris-versicolor (t(98)=, p=).

# now compare setosa petal widths to virginica widths 
#-- Setosa vs Virginica-------------
# # perform t test
# test if data satisfies assumptions for t test e.g. normal distribution and equal variance for categorial iv = names and continous dv = lengths/widths

#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the setosa petal widths is the same as the mean of the virginica petal widths coming from the same population
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the setosa petal widths is different from the mean of the virginica petal widths as the come from different populations
print("The Levene test between the Petal Widths of the Setosa and Virginica is ", stats.levene(setosa['petalW'], virginica['petalW']))
#
# test not significant as p>0.05

#check if sepal width look normally distributed - setosa done already
virginica['petalW'].plot(kind="hist", title= "Virginica Petall Width", color="red")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/virginicapetalW.jpg')
plt.show()
# histograms look to be normal distribution

# use q-q plot to see if data follows the red line. setosa done already
stats.probplot(virginica['petalW'], dist="norm", plot= plt)
plt.title("Virginica Petal Width Q-Q Plot")
plt.savefig("../graphs/virginicaPW_qqplot.jpg")
plt.show()
#data looks ok in virginica

# test virginica for normality with Shapiro-Wilk test. setosa done already
print("The Shapiro Wilk test of the Petal Widths of the Virginica is ", stats.shapiro(virginica['petalW']))
# 

#do t test
print("The t test between setosa and virginica petal widths is ", stats.ttest_ind(setosa['petalW'], virginica['petalW']))

# p<0.05 so signifant there for reject null hypothesis H0 for HA that the populations are different. 

print("The mean of the Setosa Petal Width is ",round(np.mean(setosa['petalW']),3))
print("The standard deviation of the Setosa petal Width is ", round(np.std(setosa['petalW']),3))
print("The mean of the versicolor petal Width is ",round(np.mean(versicolor['petalW']),3))
print("The standard deviation of the versicolor petal Width is ", round(np.std(versicolor['petalW']),3))

#This tested if there is a significant difference in petal widths between the Iris setosa and Iris virginica. The Iris setosa’s average petal width (M= , SD= ) is wider and has greater variation than Iris-virginica (M= , SD=). Levene’s test for homogeneity of variances indicated equality of variance (F= , p=); therefore an Independent t-test was used. Results showed a significant difference in sepal widths between Iris-setosa and Iris-virginica (t(98)=, p=).

# compare virginica to versicolor
#-- Versicolor vs Virginica-------------

#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the versicolor petal widths is the same as the mean of the virginica petal widths coming from the same population
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the versicolor  petal widths is different from the mean of the virginica petal widths as they come from different populations

print("The Levene test for Sepal Lengths of versicolor and virginica is ", stats.levene(versicolor['petalW'], virginica['petalW']))
#
# test not significant as p>0.05
#other tests done already
#do t test
print("The t test between the petal widths of Versicolor and Virginica is ", stats.ttest_ind(versicolor['petalW'], virginica['petalW']))
# 
print("The mean of the Versicolor petal width is ",round(np.mean(versicolor['petalW']),3))
print("The standard deviation of the Versicolor petal width is ", round(np.std(versicolor['petalW']),3))
print("The mean of the Virginica Petal Width is ",round(np.mean(virginica['petalW']),3))
print("The standard deviation of the Virginica Petal Width is ", round(np.std(virginica['petalW']),3))

#This tested if there is a significant difference in petal widths between the Iris setosa and Iris virginica. The Iris setosa’s average petal width (M= , SD= ) is wider and has greater variation than Iris-virginica (M= , SD=). Levene’s test for homogeneity of variances indicated equality of variance (F= , p=); therefore an Independent t-test was used. Results showed a significant difference in sepal widths between Iris-setosa and Iris-virginica (t(98)=, p=).

# do the same for petal lengths

#------petal lengths-----------
#-- Setosa vs Versicolor------
# perform t test
# test if data satisfies assumptions for t test e.g. normal distribution and equal variance for categorial iv = names and continous dv = lengths/widths

#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the setosa petal lengths the same as the mean of the versicolor sepal lengths coming from the same population
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the setosa petal lengths is different from the mean of the versicolor petal lengths as they come from different populations
print("The Levene test between Petal Lengths of the Setosa and Versicolor is ", stats.levene(setosa['petalL'], versicolor['petalL']))
#
# test not significant as p>0.05

#check if petal widths look normally distributed
setosa['petalL'].plot(kind="hist", title="Setosa Petal Length")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/setosapetalL.jpg')
plt.show()
versicolor['petalL'].plot(kind="hist", title= "Versicolor Petal Length", color="green")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/versicolorpetalL.jpg')
plt.show()
# histograms look to be normal distribution

# use q-q plot to see if data follows the red line. 
stats.probplot(setosa['petalL'], dist="norm", plot= plt)
plt.title("Setosa petal Length Q-Q Plot")
plt.savefig("../graphs/setosaPL_qqplot.jpg")
plt.show()
# data looks okay in setosa

stats.probplot(versicolor['petalL'], dist="norm", plot= plt)
plt.title("Versicolor Petal Length Q-Q Plot")
plt.savefig("../graphs/versicolorPL_qqplot.jpg")
plt.show()
#data looks ok in versicolor

# test setosa for normality with Shapiro-Wilk test
print("The Shapiro Wilk test for the Setosa Petal Length is ", stats.shapiro(setosa['petalL']))
# ) p>0.05 so not significant 

# test versicolor for normality with Shapiro-Wilk test
print("The Shapiro Wilk test for the Versicolor Petal Length is ", stats.shapiro(versicolor['petalL']))
# p>0.05 so not significant 

#do t test
print(stats.ttest_ind(setosa['petalL'], versicolor['petalL']))
#
#  p<0.05 so signifant there for reject null hypothesis H0 for HA that the populations are different. 

print("The mean of the Setosa Petal Length is ",round(np.mean(setosa['petalL']),3))
print("The standard deviation of the Setosa Petal Length is ", round(np.std(setosa['petalL']),3))
print("The mean of the versicolor Petal Length is ",round(np.mean(versicolor['petalL']),3))
print("The standard deviation of the versicolor petal Length is ", round(np.std(versicolor['petalL']),3))

#This tested if there is a significant difference in petal widths between the Iris setosa and Iris versicolor. The Iris setosa’s average petal width (M= , SD= ) is wider and has greater variation than Iris-versicolor (M= , SD= ). Levene’s test for homogeneity of variances indicated equality of variance (F= , p=); therefore an Independent t-test was used. Results showed a significant difference in petal widths between Iris-setosa and Iris-versicolor (t(98)=, p=).

# now compare setosa lengths to virginica lengths 
#-- Setosa vs Virginica-------------
# # perform t test
# test if data satisfies assumptions for t test e.g. normal distribution and equal variance for categorial iv = names and continous dv = lengths/widths

#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the setosa petal lengths is the same as the mean of the virginica petal lengths coming from the same population
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the setosa petal lengths is different from the mean of the virginica petal lengths as they come from different populations
print("The Levene test between Setosa and Virginica petal lengths is ", stats.levene(setosa['petalL'], virginica['petalL']))
#
# test not significant as p>0.05

#check if sepal width look normally distributed - setosa done already
virginica['petalL'].plot(kind="hist", title= "Virginica Petal Length", color="red")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/virginicapetalL.jpg')
plt.show()
# histograms look to be normal distribution

# use q-q plot to see if data follows the red line. setosa done already
stats.probplot(virginica['petalL'], dist="norm", plot= plt)
plt.title("Virginica Petal Length Q-Q Plot")
plt.savefig("../graphs/virginicaPL_qqplot.jpg")
plt.show()
#data looks ok in virginica

# test virginica for normality with Shapiro-Wilk test. setosa done already
print("The Shapiro-Wilk test for the Setosa Petal Length is ", stats.shapiro(virginica['petalL']))
#  p>0.05 so not significant

#do t test
print("The t-test between the Setosa and Virginica petal length is ", stats.ttest_ind(setosa['petalL'], virginica['petalL']))
#  p<0.05 so significant there for reject null hypothesis H0 for HA that the populations are different. 

print("The mean of the Setosa Petal Length is  ",round(np.mean(setosa['petalL']),3))
print("The standard deviation of the Setosa Petal Length is ", round(np.std(setosa['petalL']),3))
print("The mean of the Virginica Petal Length is ",round(np.mean(virginica['petalL']),3))
print("The standard deviation of the virginica petal length is ", round(np.std(virginica['petalL']),3))

#This tested if there is a significant difference in petal lenghts between the Iris setosa and Iris virginica. The Iris setosa’s average petal length (M= , SD= ) is wider and has greater variation than Iris-virginica (M=, SD=). Levene’s test for homogeneity of variances indicated equality of variance (F= , p=); therefore an Independent t-test was used. Results showed a significant difference in petal lenghts between Iris-setosa and Iris-virginicaersicolor (t(98)=, p=).

# compare virginica to versicolor
#-- Versicolor vs Virginica-------------
#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the versicolor petal lengths is the same as the mean of the virginica petal lengths coming from the same population
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the versicolor petal lengths is different from the mean of the virginica petal lengths as the come from different populations

print("The Levene test for Sepal Lengths of versicolor and virginica is ", stats.levene(versicolor['petalL'], virginica['petalL']))
#
# test not significant as p>0.05
#other tests done already
#do t test
print("The t test between the sepal lengths of Versicolor and Virginica is ", stats.ttest_ind(versicolor['petalL'], virginica['petalW']))
# 
print("The mean of the Versicolor petal length is ",round(np.mean(versicolor['petalL']),3))
print("The standard deviation of the Versicolor petal length is ", round(np.std(versicolor['petalL']),3))
print("The mean of the Virginica Petal length is ",round(np.mean(virginica['petalL']),3))
print("The standard deviation of the Virginica Petal length is ", round(np.std(virginica['petalL']),3))

#This tested if there is a significant difference in petal lengths between the Iris versicolor and Iris virginica. The Iris versicolor's average sepal width (M= , SD= ) is wider and has greater variation than Iris-virginica (M= , SD=). Levene’s test for homogeneity of variances indicated equality of variance (F= , p=); therefore an Independent t-test was used. Results showed a significant difference in sepal widths between Iris-setosa and Iris-virginica (t(98)=, p=).

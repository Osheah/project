#Helen O'Shea 22/03/2018 
# code adapted and expanded from https://pythonfordatascience.org/independent-t-test-python/

# This file contains the code to test the Iris data inferencial statistics. It aims to test sepal and petal lengths and widths for the various categories of iris, setosa, versicolor and virginica, with an indpendent/depenent t-test depending on applicableness. 
  
# Load libraries
import pandas as pd # get pandas
import numpy as np # get numpy
from scipy import stats # get scipy - did I use this? not sure
import matplotlib.pyplot as plt # get matplotlib.pyplot


# Load iris data and separate out by species name
url = "../data/iris.csv" # location of data 
names = ['sepalL', 'sepalW', 'petalL', 'petalW', 'name'] # add the names of the headings
iris = pd.read_csv(url, names=names) # imports the data from the local data folder  and gives it the headings listed in names

#split iris data up by category 

iris.groupby("name")["sepalL"].describe()
setosa=iris[(iris['name'] == 'Iris-setosa')] # just the setosa data
versicolor=iris[(iris['name'] == 'Iris-versicolor')] # just the versicolor data
virginica=iris[(iris['name'] == 'Iris-virginica')] # just the virginica data


#---------Sepals---------------------

#---------Sepal Widths---------------

#-- Setosa vs Versicolor-------------

#test assumptions
# test if data satisfies assumptions for t test e.g. 
# 1. normal distribution 
# 2. equal variance for categorial iv = names and continous dv = lengths/widths

#The hypothesis under investigation is 

# Null hypothesis (H0): u1 = u2, ie the mean of the setosa sepal widths is the same as the mean of the versicolor sepal widths i.e. they come from the same population distribution. 

# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the setosa sepal widths is different from the mean of the versicolor sepal widths i.e. They come from different populations

# apply levene test for equal variance

print("The Levene test for Sepal Widths of Setosa and Versicolor is ", stats.levene(setosa['sepalW'], versicolor['sepalW']))
#LeveneResult(statistic=0.66354593329432332, pvalue=0.41728596812962038)
# test is not significant as p>0.05

#check if sepal widths look normally distributed with histogram, label axis
# check setosa
setosa['sepalW'].plot(kind="hist", title="Setosa Sepal Width")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/setosasepalW.jpg') # save graph
#plt.show() # show graph - remove this later
# check versicolor

versicolor['sepalW'].plot(kind="hist", title= "Versicolor Sepal Width", color="green")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/versicolorsepalW.jpg') # save graph
#plt.show() #show graph

# histograms could be from a normal distribution
# use q-q plot to see if data follows the red line. 
stats.probplot(setosa['sepalW'], dist="norm", plot= plt)
plt.title("Setosa Sepal Width Q-Q Plot")
plt.savefig("../graphs/setosaSW_qqplot.jpg") # save graph
#plt.show() # show graph
# data looks okay in setosa around central values but moves away from line at end points.

# use qq plot to see if versicolor follows the red line = normal distribution
stats.probplot(versicolor['sepalW'], dist="norm", plot= plt)
plt.title("Versicolor Sepal Width Q-Q Plot")
plt.savefig("../graphs/versicolorSW_qqplot.jpg") # save graph
plt.show() # show graph
# data looks okay in versicolor but deviates from line at end points

# test setosa for normality with Shapiro-Wilk test - significant value => not normally distributed

print("The Shapiro Wilk test for normal distribution for the Setosa Sepal Widths is ",stats.shapiro(setosa['sepalW'])) # get value
#  (0.968691885471344, 0.20465604960918427)
# this is not significant as p>0.05 so assume normal distribution and can use setosa sepal widths in t test as assumption 1 and 2 satisfied

# test versicolor for normality with Shapiro-Wilk test
print("The Shapiro Wilk test for normal distribution for the Versicolor Sepal Widths is ", stats.shapiro(versicolor['sepalW']))
# Widths is  (0.9741330742835999, 0.33798879384994507)
# this is not significant as p>0.05 so assume normal distribution and can use versicolor sepal widths in t test as assumption 1 and 2 satisfied 

#do independent t test
print("The t test between the setosa and versicolor sepal widths is ", stats.ttest_ind(setosa['sepalW'], versicolor['sepalW']))
# Ttest_indResult(statistic=9.2827725555581111, pvalue=4.3622390160102143e-15)

# get the values for the write up - save scrolling back up but not needed as calcs are in desc.py
print("The mean of the Setosa Sepal Width is ",round(np.mean(setosa['sepalW']),3))#3.418
print("The standard deviation of the Setosa Sepal Width is ", round(np.std(setosa['sepalW']),3)) #0.377
print("The mean of the versicolor Sepal Width is ",round(np.mean(versicolor['sepalW']),3)) # 2.77
print("The standard deviation of the versicolor Sepal Width is ", round(np.std(versicolor['sepalW']),3)) #0.311
# write up results
#Results Setosa sepal widths against Versicolor Sepal widths
#This tested if there is a significant difference in sepal widths between the Iris setosa and Iris versicolor. The Iris setosa’s average sepal width (M=3.418 , SD= 0.377) is wider and has greater variation than Iris-versicolor (M= 2.77, SD=0.311). Levene’s test for homogeneity of variances indicated equality of variance (F=1.057 , p=0.306); therefore an Independent t-test was used. Results showed a significant difference in sepal widths between Iris-setosa and Iris-versicolor (t(98)=9.283, p=4.362e-15). 


# now compare setosa sepal widths to virginica widths 

# #-- Setosa vs Virginica-------------
# test assumptions 1 normal distribution and 2 equality of variances

#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the setosa sepal widths is the same as the mean of the virginica sepal widths

# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the setosa sepal widths is different from the mean of the virginica sepal widths 

# test for equal variances with levene test
print("The Levene test for Sepal Widths of setosa and virginica is ", stats.levene(setosa['sepalW'], virginica['sepalW']))
#LeveneResult(statistic=1.0574747096290729, pvalue=0.30632327568956708)
#This is not significant as p>0.05 so assumption 2 is satisfied 

#check if sepal width look normally distributed - setosa done already
virginica['sepalW'].plot(kind="hist", title= "Virginica Sepal Width", color="red")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/virginicasepalW.jpg') # save graph
#plt.show() # show graph
# histogram could be from a normal distribution - assumpiton 1

# use q-q plot to see if data follows the red line. setosa done already
stats.probplot(virginica['sepalW'], dist="norm", plot= plt)
plt.title("Virginica Sepal Width Q-Q Plot")
plt.savefig("../graphs/virginicaSW_qqplot.jpg") # save graph
#plt.show() # show graph
#data looks ok in virginica around the central values but deviates at end points. assumption 1. 

# test virginica for normality with Shapiro-Wilk test. setosa done already
print("The Shapiro Wilk test of Virginica Sepal Widths is ", stats.shapiro(virginica['sepalW']))
# (0.9673910140991211, 0.1809043288230896) this is not significant as p>0.05
# Assumption 1 and 2 okay so..
#do t test - independent t-test; 
print("The t test between the sepal widths of Setosa and Virginica is ", stats.ttest_ind(setosa['sepalW'], virginica['sepalW']))
# Ttest_indResult(statistic=6.2893849966720614, pvalue=8.9166340670064427e-09)
#This is significant as p<0.05

# this is here for convience only as data already calculated in desc.py
print("The mean of the Setosa Sepal Width is ",round(np.mean(setosa['sepalW']),3)) #3.418
print("The standard deviation of the Setosa Sepal Width is ", round(np.std(setosa['sepalW']),3))#0.377
print("The mean of the Virginica Sepal Width is ",round(np.mean(virginica['sepalW']),3))#2.974
print("The standard deviation of the Virginica Sepal Width is ", round(np.std(virginica['sepalW']),3))#0.319

#write up results
#This tested if there is a significant difference in sepal widths between the Iris setosa and Iris virginica. The Iris setosa’s average sepal width (M=3.418 , SD=0.377 ) is wider and has slightly greater variation than Iris-virginica (M= 2.974, SD=0.319). Levene’s test for homogeneity of variances indicated equality of variance (F= 0.967, p=0.181); therefore an Independent t-test was used. Results showed a significant difference in sepal widths between Iris-setosa and Iris-virginica (t(98)=6.289, p=8.917e-09).

#--Versicolor vs Virginica-------------
# compare virginica to versicolor sepal widths

#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the versicolor sepal width is the same as the mean of the virginica sepal width

# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the versicolor  sepal widths is different from the mean of the virginica sepal widths 
# Check assumptions
# check for equal variance with levene test

print("The Levene test for Sepal Widths of versicolor and virginica is ", stats.levene(versicolor['sepalW'], virginica['sepalW']))
#LeveneResult(statistic=0.087266251113089707, pvalue=0.7683067284841042)
# test not significant as p>0.05
#other tests done already and were okay

#do t test  - independent t-test
print("The t test between the sepal widths of Versicolor and Virginica is ", stats.ttest_ind(versicolor['sepalW'], virginica['sepalW']))
#Ttest_indResult(statistic=-3.2057607502218186, pvalue=0.0018191004238894803)

# get descriptive stats - here for convience only as already calculated in desc.py

print("The mean of the Versicolor Sepal Width is ",round(np.mean(versicolor['sepalW']),3))#2.77
print("The standard deviation of the Versicolor Sepal Width is ", round(np.std(versicolor['sepalW']),3))#0.311
print("The mean of the Virginica Sepal Width is ",round(np.mean(virginica['sepalW']),3))#2.974
print("The standard deviation of the Virginica Sepal Width is ", round(np.std(virginica['sepalW']),3))#0.319

# write up results
#This tested if there is a significant difference in sepal widths between the Iris versicolor and Iris virginica. The Iris versicolor’s average sepal width (M=2.77 , SD=0.311 ) is shorter slightly smaller variation than Iris-virginica (M=2.974 , SD=0.319). Levene’s test for homogeneity of variances indicated equality of variance (F=0.087 , p=0.768); therefore an Independent t-test was used. Results showed a significant difference in sepal widths between Iris-versicolor and Iris-virginica (t(98)=3.206, p=0.002).

#---------- end of sepal width tests

# do the same for sepal lengths

##------sepal lengths-----------
#-- Setosa vs Versicolor--------
# 
# test assumptions 1 Normal dist  and 2 equal variance 

#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the setosa sepal lengths the same as the mean of the versicolor sepal lengths 
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the setosa sepal lengths is different from the mean of the versicolor sepal lengths 

# test for equal variance
print("The Levene test for sepal lengths between the Setosa and Versicolor is ", stats.levene(setosa['sepalL'], versicolor['sepalL']))
#LeveneResult(statistic=8.1727205337286826, pvalue=0.0051955216310175262)
# the test is significant as p<0.05 so use welch-t-test for unequal variance

#check if sepal widths look normally distributed
setosa['sepalL'].plot(kind="hist", title="Setosa Sepal Length")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/setosasepalL.jpg') # save graph
#plt.show() # show graph
# histogram looks normal

# check versicolor sepal lengths
versicolor['sepalL'].plot(kind="hist", title= "Versicolor Sepal Length", color="green")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/versicolorsepalL.jpg') # save graph
#plt.show() # show graph
# histograms could be from a normal distribution but looks skewed to the right. 

# use q-q plot to see if data follows the red line. 
stats.probplot(setosa['sepalL'], dist="norm", plot= plt)
plt.title("Setosa Sepal Length Q-Q Plot")
plt.savefig("../graphs/setosaSL_qqplot.jpg") # save graph
#plt.show() # show graph
# data looks okay in setosa around central values. 

stats.probplot(versicolor['sepalL'], dist="norm", plot= plt)
plt.title("Versicolor Sepal Length Q-Q Plot")
plt.savefig("../graphs/versicolorSL_qqplot.jpg") # save graph
#plt.show() # show graph
#data looks ok in versicolor around central values, possibly ossolating around the red line

# test setosa for normality with Shapiro-Wilk test
print("The Shapiro Wilk test for the sepal lengths of the Setosa is", stats.shapiro(setosa['sepalL']))
# (0.9776989221572876, 0.4595281183719635)
#p is not significant as p>0.05 so assume normal distribution.

# test versicolor for normality with Shapiro-Wilk test
print("The Shapiro Wilk test for the sepal lengths of the Versicolor is ", stats.shapiro(versicolor['sepalL']))
#(0.9778355956077576, 0.46473264694213867)
#p is not significant as p>0.05 so assume normal distribution

#do t test for unequal variance
print("The t-test between the sepal lengths of the Setosa and Versicolor is ", stats.ttest_ind(setosa['sepalL'], versicolor['sepalL'], equal_var=False))
#Ttest_indResult(statistic=-10.520986267549111, pvalue=3.7467426139838419e-17)
# define welch t test 
#----- Welch t test---------------
# define welch t test to get deg of freedom and p
#code taken from https://pythonfordatascience.org/welch-t-test-python-pandas/
def welch_ttest(x, y): 
    ## Welch-Satterthwaite Degrees of Freedom ##
    dof = (x.var()/x.size + y.var()/y.size)**2 / ((x.var()/x.size)**2 / (x.size-1) + (y.var()/y.size)**2 / (y.size-1))
   
    t, p = stats.ttest_ind(x, y, equal_var = False)
    
    print("\n",
          f"Welch's t-test= {t:.4f}", "\n",
          f"p-value = {p:.4f}", "\n",
          f"Welch-Satterthwaite Degrees of Freedom= {dof:.4f}")
#call the function
print("Welch's t test between the sepal lengths of the Setosa and Versicolor is ", welch_ttest(setosa['sepalL'], versicolor['sepalL']))
#Welch's t-test= -10.5210 ,  p-value = 0.0000 ,  Welch-Satterthwaite Degrees of Freedom= 86.5380

# get descriptive stats for the write up - calcs already done in desc.py 
print("The mean of the Setosa Sepal length is ",round(np.mean(setosa['sepalL']),3))#5.006
print("The standard deviation of the Setosa Sepal length is ", round(np.std(setosa['sepalL']),3))#0.349
print("The mean of the versicolor Sepal Length is ",round(np.mean(versicolor['sepalL']),3))#5.936
print("The standard deviation of the versicolor Sepal Length is ", round(np.std(versicolor['sepalL']),3))

#  Write up
#This tested if there is a significant difference in sepal lengths between the Iris setosa and Iris versicolor. The Iris setosa’s average sepal length (M=5.006, SD=0.349) is smaller and has less variation than Iris-versicolor (M=5.936 , SD=0.511). Levene’s test for homogeneity of variances was significant (F=8.172, p<0.05); therefore an Welch's t-test was used. Results showed a significant difference in sepal widths between Iris-setosa and Iris-versicolor (t(86.538)=-10.521, p<0.05). 

# now compare setosa widths to virginica widths 

#-- Setosa vs Virginica-------------
# # perform t test
# test if data satisfies assumptions for t test e.g. normal distribution and equal variance for categorial iv = names and continous dv = lengths/widths

#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the setosa sepal lengths is the same as the mean of the virginica sepal lengths 
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the setosa sepal lengths is different from the mean of the virginica sepal lengths 

# check for equal variance assumption 2
print("The levene test for between the Setosa and Virginca sepal lengths is ", stats.levene(setosa['sepalL'], virginica['sepalL']))
#(statistic=11.454002162818494, pvalue=0.0010271363228426178)
# test significant as p<0.05 so use welch t test if applicable

#check if sepal width look normally distributed - setosa done already and was okay
virginica['sepalL'].plot(kind="hist", title= "Virginica Sepal Length", color="red")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/virginicasepalL.jpg') # save graph
#plt.show() # show graph
# histograms could be from a normal distribution though some left skewness

# use q-q plot to see if data follows the red line. setosa done already and was okay
stats.probplot(virginica['sepalL'], dist="norm", plot= plt)
plt.title("Virginica Sepal Length Q-Q Plot")
plt.savefig("../graphs/virginicaSL_qqplot.jpg") # save graph
#plt.show() # show graph
#data looks ok in virginica round central values but deviates at end ponts. 

# test virginica for normality with Shapiro-Wilk test. setosa done already
print("The Shapiro Wilks test on the Virginia sepal lengths is ", stats.shapiro(virginica['sepalL']))
# (0.9711798429489136, 0.25832483172416687) 
# test is not significant as p>0.05 so assume normal distribution

#do t test for unequal variance
print("The t-test between the Setosa and Virginica Sepal Lengths is ", stats.ttest_ind(setosa['sepalL'], virginica['sepalL'], equal_var= False))
#  Ttest_indResult(statistic=-15.386195820079404, pvalue=3.9668672709859296e-25)

print(welch_ttest(setosa['sepalL'], virginica['sepalL']))
#Welch's t-test= -15.3862 ,  p-value = 0.0000 ,  Welch-Satterthwaite Degrees of Freedom= 76.5159

# calc descriptive data for write up - not needed as already done in desc.py
print("The mean of the Setosa Sepal Length is ",round(np.mean(setosa['sepalL']),3))#5.006
print("The standard deviation of the Setosa Sepal Length is ", round(np.std(setosa['sepalL']),3))#0.349
print("The mean of the Virginica Sepal Length is ",round(np.mean(virginica['sepalL']),3))#6.588
print("The standard deviation of the Virginica Sepal Length is ", round(np.std(virginica['sepalL']),3))#0.629

# write up results
#This tested if there is a significant difference in sepal lengths between the Iris setosa and Iris virginica. The Iris setosa’s average sepal length (M= 5.006, SD=0.349 ) is smaller and has less variation than Iris-virginica (M=6.588 , SD=0.629). Levene’s test for homogeneity of variances was significant (F=11.454 , p=0.001); therefore Welsh's t-test was used. Results showed a significant difference in sepal lengths between Iris-setosa and Iris-virginica (t(76.516)=-15.386, p<0.05).

# compare virginica to versicolor
#-- Versicolor vs Virginica-------------
#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the versicolor sepal widths is the same as the mean of the virginica sepal lengths
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the versicolor sepal lengths is different from the mean of the virginica sepal lengths

# check for equal variance 
print("The Levene test for Sepal Lengths of versicolor and virginica is ", stats.levene(versicolor['sepalL'], virginica['sepalL']))
#LeveneResult(statistic=1.0245224574083649, pvalue=0.31394122
# test not significant as p>0.05

#other tests done already and normal distribution okay

#do t test - equal variance
print("The t test between the sepal lengths of Versicolor and Virginica is ", stats.ttest_ind(versicolor['sepalL'], virginica['sepalL']))
#Ttest_indResult(statistic=-5.6291652597198008, pvalue=1.7248563024547942e-07)

# get descriptive stats for convience only as already in desc.py
print("The mean of the Versicolor sepal length is ",round(np.mean(versicolor['sepalL']),3))#5.936
print("The standard deviation of the Versicolor Sepal length is ", round(np.std(versicolor['sepalL']),3))#0.511
print("The mean of the Virginica Sepal Length is ",round(np.mean(virginica['sepalL']),3))#6.588
print("The standard deviation of the Virginica Sepal length is ", round(np.std(virginica['sepalL']),3))#0.629

#write up results
#This tested if there is a significant difference in sepal lengths between the Iris versicolor and Iris virginica. The Iris versicolor's average sepal length (M=5.936 , SD=0.511 ) is shorter and has slightly less variation than Iris-virginica (M=6.588 , SD=0.629). Levene’s test for homogeneity of variances indicated equality of variance (F=1.025 , p=0.314); therefore an Independent t-test was used. Results showed a significant difference in sepal widths between Iris-versicolor and Iris-virginica (t(98)=-5.629, p=1.725).
#--------------------end of sepal tests---------------------

#-------------Petals------
#------------petal widths--

# perform t test
# test if data satisfies assumptions for t test e.g. normal distribution and equal variance for categorial iv = names and continous dv = lengths/widths

#-- Setosa vs Versicolor-------------
#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the petal widths is the same as the mean of the versicolor petal widths
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the setosa petal widths is different from the mean of the versicolor petal widths 

#check for equal variances
print("The Levene test between the Petal widths of the Setosa and Versicolor is ", stats.levene(setosa['petalW'], versicolor['petalW']))
#LeveneResult(statistic=15.188767812238058, pvalue=0.00017803544621676766)
# test significant as p<0.05 so variance is unequal hence welch t if applicable. 

#check if sepal widths look normally distributed
setosa['petalW'].plot(kind="hist", title="Setosa Petal Width")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/setosapetalW.jpg') # save graph
#plt.show() # show graph
#it could be a normal distrubion but does not look symetrical around centre. 

versicolor['petalW'].plot(kind="hist", title= "Versicolor Petal Width", color="green")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/versicolorpetalW.jpg')# save graph
#plt.show() # show graph
#This data does not look normal, maybe bimodal or higher

# use q-q plot to see if data follows the red line. 
stats.probplot(setosa['petalW'], dist="norm", plot= plt)
plt.title("Setosa Petal Width Q-Q Plot")
plt.savefig("../graphs/setosaPW_qqplot.jpg")
plt.show()
# data does not cluster around the red line - does not appear to be normal distribution

stats.probplot(versicolor['petalW'], dist="norm", plot= plt)
plt.title("Versicolor Petal Width Q-Q Plot")
plt.savefig("../graphs/versicolorPW_qqplot.jpg")
plt.show()
#data follows line but is spread out

# test setosa for normality with Shapiro-Wilk test
print("The Shapiro Wilks test of the Setosa Petal Widths is ", stats.shapiro(setosa['petalW']))
#(0.8138170838356018, 1.8525804534874624e-06) 
# p<0.05 so significant so data appears not to be normally distributed


# test versicolor for normality with Shapiro-Wilk test
print("The Shapiro Wilks test of the Versicolor Petal Widths is ", stats.shapiro(versicolor['petalW']))
#(0.947626531124115, 0.027278218418359756)
#  p<0.05 so significant so data appears not to be normally distributed

#hence cant do t test - what reasons for non normality - outliers, skewness, errors in data or bimodal distriubution?
# get the desc data for write up but note that no test was performed
print("The mean of the Setosa Petal Width is ",round(np.mean(setosa['petalW']),3))#0.244
print("The standard deviation of the Setosa Petal Width is ", round(np.std(setosa['petalW']),3))#0.106
print("The mean of the versicolor petal Width is ",round(np.mean(versicolor['petalW']),3))#0.106
print("The standard deviation of the Versicolor petal Width is ", round(np.std(versicolor['petalW']),3))#1.326

# write up the not tested data
#This tested if there is a significant difference in petal widths between the Iris setosa and Iris versicolor. The Iris setosa’s average petal width (M= 0.244, SD=0.106 ) is wider and has greater variation than Iris-versicolor (M=0.106 , SD=1.326 ). Levene’s test for homogeneity of variances was significant and both the setosa and versicolor failed the Shapiro Wilks test for normal distribution hence no t test was performed. 

# now compare setosa petal widths to virginica widths 

#-- Setosa vs Virginica-------------
# # perform t test
# test if data satisfies assumptions for t test e.g. normal distribution and equal variance for categorial iv = names and continous dv = lengths/widths

#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the setosa petal widths is the same as the mean of the virginica petal widths
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the setosa petal widths is different from the mean of the virginica petal widths

# check for equal variance
print("The Levene test between the Petal Widths of the Setosa and Virginica is ", stats.levene(setosa['petalW'], virginica['petalW']))
#LeveneResult(statistic=38.10704049844238, pvalue=1.5172074767960998e-08)
# test significant as p<0.05 so variance unequal

#check if petal width look normally distributed - setosa appears not to be normally distrubuted. 
virginica['petalW'].plot(kind="hist", title= "Virginica Petall Width", color="red")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/virginicapetalW.jpg')
#plt.show()
# histogram does not look normally distrubuted

# use q-q plot to see if data follows the red line. setosa done already and failed
stats.probplot(virginica['petalW'], dist="norm", plot= plt)
plt.title("Virginica Petal Width Q-Q Plot")
plt.savefig("../graphs/virginicaPW_qqplot.jpg") # save graph
#plt.show # show graph
#data is on the line but quite spead out rond central values. 

# test virginica for normality with Shapiro-Wilk test. setosa done already and failed
print("The Shapiro Wilk test of the Petal Widths of the Virginica is ", stats.shapiro(virginica['petalW']))

# (0.9597718715667725, 0.08695744723081589)
#test not significant as p>0.05

#however we cannot do t test as setosa petal widths appaer not to follow a normal distrubution 
# get desc calc for write up
print("The mean of the Setosa Petal Width is ",round(np.mean(setosa['petalW']),3))#0.244
print("The standard deviation of the Setosa petal Width is ", round(np.std(setosa['petalW']),3))#0.106
print("The mean of the virginica petal Width is ",round(np.mean(virginica['petalW']),3))#2.026
print("The standard deviation of the virginica petal Width is ", round(np.std(virginica['petalW']),3))#0.272

#write up the non result
#This tested if there is a significant difference in petal widths between the Iris setosa and Iris virginica. The Iris setosa’s average petal width (M=0.244,  SD=0.106 ) is smaller and has less variation than Iris-virginica (M=2.026 , SD=0.272). Levene’s test for homogeneity of variances was significant (F=38.107, p=1.517e-8); The Shapiro Wilk for the Iris setosa petal widths was significant (F=0.814, p=1.853e-06) whereas the Shapiro Wilk test for the Iris Virginica was not significant (F=0.960, p=0.09) therefore no t test was performed. 

# compare virginica to versicolor
#-- Versicolor vs Virginica-------------

#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the versicolor petal widths is the same as the mean of the virginica petal widths 
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the versicolor  petal widths is different from the mean of the virginica petal widths

# check for equal variance 
print("The Levene test for petal Lengths of versicolor and virginica is ", stats.levene(versicolor['petalW'], virginica['petalW']))
#LeveneResult(statistic=6.5454545454545485, pvalue=0.012046123630720964)
# test significant as p<0.05 so variance is unequal

#other tests done already - versicolor was significant for Sharpio Wilk test so cant do test. 

# get descriptive stats for write up for convience only
print("The mean of the Versicolor petal width is ",round(np.mean(versicolor['petalW']),3))#1.326
print("The standard deviation of the Versicolor petal width is ", round(np.std(versicolor['petalW']),3))#0.196
print("The mean of the Virginica Petal Width is ",round(np.mean(virginica['petalW']),3))#2.026
print("The standard deviation of the Virginica Petal Width is ", round(np.std(virginica['petalW']),3))#0.272

#write up the non test
#This tested if there is a significant difference in petal widths between the Iris versicolor and Iris virginica. The Iris versicolor's average petal width (M=1.326 , SD=0.196) is smaller and has less variation than Iris-virginica (M=2.026 , SD=0.272). Levene’s test for homogeneity of variances was significant (F=6.546, p=0.012) and the versicolor failed the Shapiro Wilks test for normal distribution hence no t test was performed. 

#----------------end of petal widths---------

# do the same for petal lengths

#------petal lengths-----------

#-- Setosa vs Versicolor------
# perform t test
# test if data satisfies assumptions for t test e.g. normal distribution and equal variance for categorial iv = names and continous dv = lengths/widths

#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the setosa petal lengths the same as the mean of the versicolor sepal lengths 
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the setosa petal lengths is different from the mean of the versicolor petal lengths

# check assumption of equal variance
print("The Levene test between Petal Lengths of the Setosa and Versicolor is ", stats.levene(setosa['petalL'], versicolor['petalL']))
#LeveneResult(statistic=30.897026860775114, pvalue=2.3481003006595618e-07)
# test is significant as p<0.05 so variance is unequal

#check if petal widths look normally distributed
setosa['petalL'].plot(kind="hist", title="Setosa Petal Length")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/setosapetalL.jpg') # save graph
#plt.show() # show graph
# looks normally distrubuted

versicolor['petalL'].plot(kind="hist", title= "Versicolor Petal Length", color="green")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/versicolorpetalL.jpg') # save graph
#plt.show() # show graph
# histogram looks skewed to the left. 

# use q-q plot to see if data follows the red line. 
stats.probplot(setosa['petalL'], dist="norm", plot= plt)
plt.title("Setosa petal Length Q-Q Plot")
plt.savefig("../graphs/setosaPL_qqplot.jpg") # save graph
# plt.show() # show graph
# data follows the line but is not clustered around it at central values. 

stats.probplot(versicolor['petalL'], dist="norm", plot= plt)
plt.title("Versicolor Petal Length Q-Q Plot")
plt.savefig("../graphs/versicolorPL_qqplot.jpg") # save graph
# plt.show() # show graph
#data could be from a normal distribution but shows signs of skewness to the left. 

# test setosa for normality with Shapiro-Wilk test
print("The Shapiro Wilk test for the Setosa Petal Length is ", stats.shapiro(setosa['petalL']))
# (0.9549458622932434, 0.05464918911457062)
# p>0.05 so not significant but only just!!

# test versicolor for normality with Shapiro-Wilk test
print("The Shapiro Wilk test for the Versicolor Petal Length is ", stats.shapiro(versicolor['petalL']))
#(0.9660047888755798, 0.1584833413362503)
# p>0.05 so not significant 

#do t test with unequal variance
print(stats.ttest_ind(setosa['petalL'], versicolor['petalL'], equal_var= False))
#Ttest_indResult(statistic=-39.468662593972709, pvalue=1.057210030060334e-45)
#  p<0.05. 

#Do Welch's t-test
print(welch_ttest(setosa['petalL'], versicolor['petalL']))
# Welch's t-test= -39.4687 ,  p-value = 0.0000 ,  Welch-Satterthwaite Degrees of Freedom= 62.1175
# get the descriptive info 
print("The mean of the Setosa Petal Length is ",round(np.mean(setosa['petalL']),3))#1.464
print("The standard deviation of the Setosa Petal Length is ", round(np.std(setosa['petalL']),3))#0.172
print("The mean of the versicolor Petal Length is ",round(np.mean(versicolor['petalL']),3))#4.26
print("The standard deviation of the versicolor petal Length is ", round(np.std(versicolor['petalL']),3))#0.465

# write up results
#This tested if there is a significant difference in petal lengths between the Iris setosa and Iris versicolor. The Iris setosa’s average petal lengths (M=1.464 , SD=0.172 ) is smaller and has less variation than Iris-versicolor (M=4.26, SD=0.465 ). Levene’s test for homogeneity of variances was significant (F=30.897 , p=2.348); therefore an Independent t-test was used. Results showed a significant difference in petal lengths between Iris-setosa and Iris-versicolor (t(62.118)=-39.469, p<0.05).

# now compare setosa lengths to virginica lengths 
#-- Setosa vs Virginica-------------
# # perform t test
# test if data satisfies assumptions for t test e.g. normal distribution and equal variance for categorial iv = names and continous dv = lengths/widths

#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the setosa petal lengths is the same as the mean of the virginica petal lengths
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the setosa petal lengths is different from the mean of the virginica petal lengths 

#check for equal variance
print("The Levene test between Setosa and Virginica petal lengths is ", stats.levene(setosa['petalL'], virginica['petalL']))
#LeveneResult(statistic=39.976667001910869, pvalue=7.6515000190799952e-09)
# test significant as p<0.05 so variance is unequal

#check if sepal width look normally distributed - setosa done already and just about passed. 

virginica['petalL'].plot(kind="hist", title= "Virginica Petal Length", color="red")
plt.xlabel("Length (cm)")
plt.savefig('../graphs/virginicapetalL.jpg') # save graph
# plt.show()
# histograms look skewed to the right. 

# use q-q plot to see if data follows the red line. setosa done already
stats.probplot(virginica['petalL'], dist="norm", plot= plt)
plt.title("Virginica Petal Length Q-Q Plot")
plt.savefig("../graphs/virginicaPL_qqplot.jpg") # save graph
#plt.show() # show graph
#data looks okish in virginica - bit off near the ends and center points 

# test virginica for normality with Shapiro-Wilk test. setosa done already
print("The Shapiro-Wilk test for the Virginica Petal Length is ", stats.shapiro(virginica['petalL']))
#(0.9621862769126892, 0.10977369546890259)
#  p>0.05 so not significant

#do t test for unequal variances
print("The t-test between the Setosa and Virginica petal length is ", stats.ttest_ind(setosa['petalL'], virginica['petalL'], equal_var=False))
#  Ttest_indResult(statistic=-49.965703359355636, pvalue=9.7138670616970964e-50)

# Do Welch's t-test
print(welch_ttest(setosa['petalL'], virginica['petalL']))
#Welch's t-test= -49.9657 ,  p-value = 0.0000 ,  Welch-Satterthwaite Degrees of Freedom= 58.5928
# get the descriptive data for write up
print("The mean of the Setosa Petal Length is  ",round(np.mean(setosa['petalL']),3))#1.464
print("The standard deviation of the Setosa Petal Length is ", round(np.std(setosa['petalL']),3))#0.172
print("The mean of the Virginica Petal Length is ",round(np.mean(virginica['petalL']),3))#5.552
print("The standard deviation of the virginica petal length is ", round(np.std(virginica['petalL']),3))#0.546

#write up test
#This tested if there is a significant difference in petal lengths between the Iris setosa and Iris virginica. The Iris setosa’s average petal length (M=1.464 , SD= 0.172) is much smaller and has less variation than Iris-virginica (M=5.552, SD=0.546). Levene’s test for homogeneity of variances was significant (F=39.977 , p=7.651e-09); therefore an Welch's t-test was used. Results showed a significant difference in petal lengths between Iris-setosa and Iris-virginica (t(58.593)=-49.9657, p<0.05).

# compare virginica to versicolor

#-- Versicolor vs Virginica-------------
#The hypothesis under investigation is 
# Null hypothesis (H0): u1 = u2, ie the mean of the versicolor petal lengths is the same as the mean of the virginica petal lengths 
# Alternative hypothesis (HA): u1 ≠ u2, ie the mean of the versicolor petal lengths is different from the mean of the virginica petal lengths 
# check for equal variance
print("The Levene test for Sepal Lengths of versicolor and virginica is ", stats.levene(versicolor['petalL'], virginica['petalL']))
#LeveneResult(statistic=1.0674381993787974, pvalue=0.30406773202289633)
# test not significant as p>0.05

#other tests (Shapiro Wilk) done already for versicolor and virginica and was not significant.  

#do t test for equal variance
print("The t test between the petal lengths of Versicolor and Virginica is ", stats.ttest_ind(versicolor['petalL'], virginica['petalW']))
#Ttest_indResult(statistic=29.02282875737281, pvalue=6.4280657868349329e-50)

# get descriptive data for write up
print("The mean of the Versicolor petal length is ",round(np.mean(versicolor['petalL']),3))#4.26
print("The standard deviation of the Versicolor petal length is ", round(np.std(versicolor['petalL']),3))#0.465
print("The mean of the Virginica Petal length is ",round(np.mean(virginica['petalL']),3))#5.552
print("The standard deviation of the Virginica Petal length is ", round(np.std(virginica['petalL']),3))#0.546

#This tested if there is a significant difference in petal lengths between the Iris versicolor and Iris virginica. The Iris versicolor's average petal length (M=4.26 , SD=0.465 ) is smaller and has less variation than Iris-virginica (M=5.552 , SD=0.546). Levene’s test for homogeneity of variances indicated equality of variance (F=1.067 , p=0.304); therefore an Independent t-test was used. Results showed a significant difference in petal lengths between Iris-versicolor and Iris-virginica (t(98)=,29.023 p=6.428e-50).

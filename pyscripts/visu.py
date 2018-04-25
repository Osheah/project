#Helen O'Shea 22/03/2018 
#visualisations of the Iris Data Set
# code adapted and expanded from
#https://www.kaggle.com/benhamner/python-data-visualizations
#https://seaborn.pydata.org/generated/seaborn.pairplot.html
#https://seaborn.pydata.org/generated/seaborn.PairGrid.html

#import packages
# import pandas for data frame
import pandas as pd
import numpy as np # import numpy for use with matplotlib and seaborn
import matplotlib.pyplot as plt # import for graphs
import seaborn as sns # import seaborn for graphs
sns.set(style="white", color_codes=True)
#Load Data
url = "../data/iris.csv"
names = ['sepalL', 'sepalW', 'petalL', 'petalW', 'name']
iris = pd.read_csv(url, names=names) # use same naming convention as in desc.py
# split data by group
iris.groupby("name")["sepalL"].describe()
setosa=iris[(iris['name'] == 'Iris-setosa')] # setosa samples
versicolor=iris[(iris['name'] == 'Iris-versicolor')] # versicolor samples
virginica=iris[(iris['name'] == 'Iris-virginica')] # virginica samples

# View Data 
print(iris.head(10)) # check data loaded and view headers - can remove this later
# View number of each species
print(iris["name"].value_counts()) # check counts - can remove this later

# Scatter plot
#-----------------with matplotlib
#1 scatterplot data using matplotlib.pyplot scatter 
iris.plot(kind="scatter", x="sepalL", y="sepalW") # label x/y axis
plt.savefig("../graphs/spsepal.jpg")# save figure before ply.show or else it saves as blank
#plt.show() # maybe remove this after testing

iris.plot(kind="scatter", x="petalL", y="petalW")
plt.savefig("../graphs/sppetal.jpg")
#plt.show()

#---------------------with seaborn

#2 similar scatter plot but with corralation seaborn
sns.jointplot(x="sepalL", y="sepalW", data=iris, size=5)
plt.savefig("../graphs/snsepal.jpg")
#plt.show()

sns.jointplot(x="petalL", y="petalW", data=iris, size=5)
plt.savefig("../graphs/snpetal.jpg")
#plt.show()


## plt does not show colours for the iris names so use seaborn to identify the types of iris
# plot 1 and 2 does show data breakdown by iris name - so plot scatter plot using seaborn
#3 scatter plot labelled by iris name
sns.FacetGrid(iris, hue="name", size=5) \
   .map(plt.scatter, "sepalL", "sepalW") \
   .add_legend()
plt.savefig("../graphs/sn2sepal.jpg")
#plt.show()   

sns.FacetGrid(iris, hue="name", size=5) \
   .map(plt.scatter, "petalL", "petalW") \
   .add_legend()
plt.savefig("../graphs/sn2petal.jpg")
#plt.show()   

# 4 Histograms
#plot histograms
#all iris data separated by dimensions
#plot histograms
plt.hist(iris['sepalW'])
plt.savefig("../graphs/iSW.jpg")
#plt.show()

plt.hist(iris['sepalL'])
plt.savefig("../graphs/iSL.jpg")
#plt.show()

plt.hist(iris['petalW'])
plt.savefig("../graphs/iPW.jpg")
#plt.show()

plt.hist(iris['petalL'])
plt.savefig("../graphs/iPL.jpg")
#plt.show()

# iris data histograms separated by species

#-----------------------------------sepals---------------------------------
# ------------------setosa
# sepal widths
plt.hist(setosa['sepalW'])
plt.savefig("../graphs/hSSW.jpg")
#plt.show()
#sepal lengths
plt.hist(setosa['sepalL'])
plt.savefig("../graphs/hSSL.jpg")
#plt.show()
#---------- versicolor
#sepal widths
plt.hist(versicolor['sepalW'])
plt.savefig("../graphs/hVeSW.jpg")
#plt.show()
#sepal lenghts
plt.hist(versicolor['sepalL'])
plt.savefig("../graphs/hVeSL.jpg")
#plt.show()
#-------------virginica
#sepal widths
plt.hist(virginica['sepalW'])
plt.savefig("../graphs/hViSW.jpg")
#plt.show()
#sepal lengths
plt.hist(virginica['sepalL'])
plt.savefig("../graphs/hViSL.jpg")
#plt.show()
#----------------------------------------------petals--------------------------
# --------------------setosa
#petal widths
plt.hist(setosa['petalW'])
plt.savefig("../graphs/hSPW.jpg")
#plt.show()

plt.hist(setosa['petalL'])
plt.savefig("../graphs/hSPL.jpg")
# petal lengths

#plt.show()
#-----------------------versicolor
#petal widths
plt.hist(versicolor['petalW'])
plt.savefig("../graphs/hVePW.jpg")
#plt.show()
# petal lengths
plt.hist(versicolor['petalL'])
plt.savefig("../graphs/hVePL.jpg")
#plt.show()
#------------------virginica
#petal widths
plt.hist(virginica['petalW'])
plt.savefig("../graphs/hViPW.jpg")
#petal lengths
#plt.show()
plt.hist(virginica['petalL'])
plt.savefig("../graphs/iPL.jpg")
#plt.show()

#5 Box plots max, min quartles and median plus outliers 
#use seaborn
sns.boxplot(x="name", y="sepalL", data=iris) 
plt.savefig("../graphs/bpsepalL.jpg")
#plt.show()
sns.boxplot(x="name", y="sepalW", data=iris) 
plt.savefig("../graphs/bpsepalW.jpg")
#plt.show()
sns.boxplot(x="name", y="petalL", data=iris) 
plt.savefig("../graphs/bppetalL.jpg")
#plt.show()
sns.boxplot(x="name", y="petalW", data=iris) 
plt.savefig("../graphs/bppetalW.jpg")
#plt.show()

#6 use a strip plot and boxplot on the same axis to look at the distribution of the data 
ax = sns.boxplot(x="name", y="sepalL", data=iris)
ax = sns.stripplot(x="name", y="sepalL", data=iris, jitter=True, edgecolor="gray")
plt.savefig("../graphs/bp2sepalL.jpg")
#plt.show() 
ax = sns.boxplot(x="name", y="sepalW", data=iris)
ax = sns.stripplot(x="name", y="sepalW", data=iris, jitter=True, edgecolor="gray")
plt.savefig("../graphs/bp2sepalW.jpg") 
#plt.show()
ax = sns.boxplot(x="name", y="petalL", data=iris)
ax = sns.stripplot(x="name", y="petalL", data=iris, jitter=True, edgecolor="gray") 
plt.savefig("../graphs/bp2petalL.jpg")
#plt.show()
ax = sns.boxplot(x="name", y="petalW", data=iris)
ax = sns.stripplot(x="name", y="petalW", data=iris, jitter=True, edgecolor="gray") 
plt.savefig("../graphs/bp2petalW.jpg")
#plt.show()

#-------------density plots-----------------------------
#7 use violin plot to visulise the density distribution of the data along with box plot measures
# the denser regions of the data are shown as thicker sections of the violin plot and sparcer regions as thinner sections of the plot  
sns.violinplot(x="name", y="sepalL", data=iris, size=6)
plt.savefig("../graphs/vpsepalL.jpg")
#plt.show()
sns.violinplot(x="name", y="sepalW", data=iris, size=6)
plt.savefig("../graphs/vpsepalW.jpg")
#plt.show()
sns.violinplot(x="name", y="petalL", data=iris, size=6)
plt.savefig("../graphs/vppetalL.jpg")
#plt.show()
sns.violinplot(x="name", y="petalW", data=iris, size=6)
plt.savefig("../graphs/vppetalW.jpg")
#plt.show()

#8 the distribution of the underlying data can be visualised by looking at the kernel density estimate kde plot
sns.FacetGrid(iris, hue="name", size=6) \
   .map(sns.kdeplot, "sepalL") \
   .add_legend()
plt.savefig("../graphs/kdesepalL.jpg")
plt.show()
sns.FacetGrid(iris, hue="name", size=6) \
   .map(sns.kdeplot, "sepalW") \
   .add_legend()
plt.savefig("../graphs/kdesepalW.jpg")
#plt.show()
sns.FacetGrid(iris, hue="name", size=6) \
   .map(sns.kdeplot, "petalL") \
   .add_legend()
plt.savefig("../graphs/kdepetalL.jpg")
#plt.show()
sns.FacetGrid(iris, hue="name", size=6) \
   .map(sns.kdeplot, "petalW") \
   .add_legend()
plt.savefig("../graphs/kdepetalW.jpg")
#plt.show()

#9 this shows the relationship between the various sepal/petal lengths/widths measures 
g = sns.pairplot(iris, hue="name")
plt.savefig("../graphs/pairploth.jpg")
#plt.show()
# similar to above but with kde along the diag instead of histograms
#
g = sns.pairplot(iris, hue="name", diag_kind="kde")
plt.savefig("../graphs/pairplotk.jpg")
#plt.show()

#10 Andrews curves are a method for visualizing multidimensional data by mapping each observation onto a function. In the plot each colour used represents a class and we can easily note that the lines that represent samples from the same class have similar curves.Andrews curves that are represented by functions close together suggest that the corresponding data points will also be close together.
from pandas.plotting import andrews_curves
andrews_curves(iris, "name")
plt.savefig("../graphs/andrewcs.jpg")
#plt.show()

#11 Another multivariate visualization technique pandas has is parallel_coordinates
# Parallel coordinates plots each feature on a separate column & then draws lines
# connecting the features for each data sample
#Inselberg (Inselberg 1997) made a full review of how to visually read out parallel coords' relational patterns.[9] When most lines between two parallel axis are somewhat parallel to each others, that suggests a positive relationship between these two dimensions. When lines cross in a kind of superposition of X-shapes, that's negative relationship. When lines cross randomly or are parallel, that show there is no particular relationship.
from pandas.plotting import parallel_coordinates
parallel_coordinates(iris, "name")
plt.savefig("../graphs/parac.jpg")
#plt.show()
#12
from pandas.plotting import radviz
radviz(iris, "name")
plt.savefig("../graphs/rad.jpg")
#plt.show()
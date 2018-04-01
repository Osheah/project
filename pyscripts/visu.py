#visualisations of the Iris Data Set
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
iris = pd.read_csv(url, names=names)

# View Data 
print(iris.head(10)) # check data loaded and view headers
# View number of each species
print(iris["name"].value_counts()) # check counts

# scatterplot data
#1
plt.scatter(iris.sepalL, iris.sepalW, s=100, c=iris.name)
plt.show()
'''
#1
iris.plot(kind="scatter", x="sepalL", y="sepalW")
iris.plot(kind="scatter", x="PetalL", y="petalW")
plt.show()
#2
sns.jointplot(x="SepalL", y="SepalW", data=iris, size=5)
plt.show()
sns.jointplot(x="PetalL", y="PetalW", data=iris, size=5)
plt.show()
#3
sns.FacetGrid(iris, hue="Species", size=5) \
   .map(plt.scatter, "SepalL", "SepalW") \
   .add_legend()
plt.show()
sns.FacetGrid(iris, hue="Species", size=5) \
   .map(plt.scatter, "PetalL", "PetalW") \
   .add_legend()   
plt.show()
#4
sns.boxplot(x="Species", y="PetalL", data=iris) 
plt.show()
sns.boxplot(x="Species", y="PetalW", data=iris) 
plt.show()
sns.boxplot(x="Species", y="SepalL", data=iris) 
plt.show()
sns.boxplot(x="Species", y="SepalW", data=iris) 
plt.show()
#5
ax = sns.boxplot(x="Species", y="PetalL", data=iris)
ax = sns.stripplot(x="Species", y="PetalL", data=iris, jitter=True, edgecolor="gray") 
plt.show()
ax = sns.boxplot(x="Species", y="PetalW", data=iris)
ax = sns.stripplot(x="Species", y="PetalW", data=iris, jitter=True, edgecolor="gray") 
plt.show()
ax = sns.boxplot(x="Species", y="SepalL", data=iris)
ax = sns.stripplot(x="Species", y="SepalL", data=iris, jitter=True, edgecolor="gray")
plt.show() 
ax = sns.boxplot(x="Species", y="SepalW", data=iris)
ax = sns.stripplot(x="Species", y="SepalW", data=iris, jitter=True, edgecolor="gray") 
plt.show()
#6
sns.violinplot(x="Species", y="PetalL", data=iris, size=6)
plt.show()
sns.violinplot(x="Species", y="PetalW", data=iris, size=6)
plt.show()
sns.violinplot(x="Species", y="SepalL", data=iris, size=6)
plt.show()
sns.violinplot(x="Species", y="SepalW", data=iris, size=6)
plt.show()

#7
sns.FacetGrid(iris, hue="Species", size=6) \
   .map(sns.kdeplot, "PetalL") \
   .add_legend()
plt.show()
sns.FacetGrid(iris, hue="Species", size=6) \
   .map(sns.kdeplot, "PetalW") \
   .add_legend()
plt.show()
sns.FacetGrid(iris, hue="Species", size=6) \
   .map(sns.kdeplot, "SepalL") \
   .add_legend()
plt.show()
sns.FacetGrid(iris, hue="Species", size=6) \
   .map(sns.kdeplot, "SepalW") \
   .add_legend()
plt.show()
#8
g = sns.pairplot(iris, hue="Species")
plt.show()
g = sns.pairplot(iris, hue="Species", diag_kind="kde")
plt.show()

#9
from pandas.tools.plotting import andrews_curves
andrews_curves(iris, "Species")
plt.show()

#10
from pandas.plotting import parallel_coordinates
parallel_coordinates(iris, "Species")
plt.show()

#11
from pandas.plotting import radviz
radviz(iris, "Species")
plt.show()
'''

#https://www.kaggle.com/benhamner/python-data-visualizations

'''# Load the data
from sklearn.datasets import load_iris
iris = load_iris()
#iris=pandas.read_csv(url)
from matplotlib import pyplot as plt
#peek = iris.head(10)
# The indices of the features that we are plotting
x_index = 0
y_index = 1

# this formatter will label the colorbar with the correct target names
formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

plt.figure(figsize=(5, 4))
plt.scatter(iris.data[:, x_index], iris.data[:, y_index], c=iris.target)
plt.colorbar(ticks=[0, 1, 2], format=formatter)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index])

plt.tight_layout()
plt.show()


#iris.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm")'''
# First, we'll import pandas, a data processing and CSV file I/O library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts.plot()
plt.show()
# We'll also import seaborn, a Python graphing library
import warnings # current version of seaborn generates a bunch of warnings that we'll ignore
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

# Next, we'll load the Iris flower dataset, which is in the 
url = "https://raw.githubusercontent.com/Osheah/project/master/data/iris.csv?token=AiEuthVKeloCkMeFSmPeZBQ6oCblwRnRks5avOiwwA%3D%3D"
names = ['SepalL', 'SepalW', 'PetalL', 'PetalW', 'Species']
iris = pd.read_csv(url, names=names)
# the iris dataset is now a Pandas DataFrame

# Let's see what's in the iris data - Jupyter notebooks print the result of the last thing you do

#print(iris.head(10))

# Press shift+enter to execute this cell
# Let's see how many examples we have of each species
#print(iris["Species"].value_counts())
# The first way we can plot things is using the .plot extension from Pandas dataframes
# We'll use this to make a scatterplot of the Iris features.
iris.plot(kind="scatter", x="SepalL", y="SepalW")
plt.show()
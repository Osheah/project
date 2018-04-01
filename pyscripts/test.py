import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
url = "../data/iris.csv" 
names = ['sepalL', 'sepalW', 'petalL', 'petalW', 'name']
iris = pd.read_csv(url, names=names)

print(iris.head(20))
a= (iris == "Iris-setosa").idxmax(axis=1)[0]
print(a)

#Helen O'Shea 11/04/2018 
# code adapted from https://plot.ly/python/anova/

# Load libraries
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm


# Load iris data
url = "../data/iris.csv" # location of data 
names = ['sepalL', 'sepalW', 'petalL', 'petalW', 'name'] # add the names of the headings
iris = pd.read_csv(url, names=names) # imports the data from the local data folder  and gives it the headings listed in names
# test if iris data is differs from a normal distribution  - one tailed or two tailed?
setosa=iris[(iris['name'] == 'Iris-setosa')]
versicolor=iris[(iris['name'] == 'Iris-versicolor')]
virginica=iris[(iris['name'] == 'Iris-virginica')]
lm_sub_defalut = smf.ols("sepalW ~ name", data=iris).fit()
lm_sub_default.summary()
lm_sub=smf.ols('sepalW ~C(name, Helmert)', data=iris).fit()
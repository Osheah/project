# adapted from https://stackoverflow.com/questions/21568451/using-chi-squared-test-for-feature-selection

# Load libraries
import numpy

from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# Load iris data
iris = load_iris()
with open 
'''
# Create features and target
X = iris.data
y = iris.target

# Convert to categorical data by converting data to integers
X = X.astype(int)

# Select two features with highest chi-squared statistics
chi2_selector = SelectKBest(chi2, k=2)
X_kbest = chi2_selector.fit_transform(X, y)
type(X_kbest)

# Show results
print('Original number of features:', X.shape[1])
print('Reduced number of features:', X_kbest.shape[1])'''


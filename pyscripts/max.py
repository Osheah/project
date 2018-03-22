#Helen O'Shea 22/03/2018 3

with open("data/iris.csv") as iris:
  header='sl    sw    pl    pw' # sl = sepal length in cm; sw = sepal width in cm pl = petal length in cm pw= petal width in cm attributes taken from http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names
  print(header)
  for line in iris: 
    data=line.split(',')[0:4]#split the lines at the comma for the first four entries
    if len(data)==4: # needed to not print out the '/n' at the end
print('{:2s}'.format(data[0]),' ','{:2s}'.format(data[1]),' ', '{:2s}'.format(data[2]),' ', '{:2s}'.format(data[3]))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("Iris.csv")
#data.head()
data.rename(columns={'SepalLengthCm':'SL','SepalWidthCm':'SW','PetalLengthCm':'PL','PetalWidthCm':'PW'},inplace=True)
iris_setosa=data[data['Species']=='Iris-setosa']
iris_versicolor=data[data['Species']=='Iris-versicolor']
iris_virginica=data[data['Species']=='Iris-virginica']

# find mean each class Sepal Width
print(np.mean(iris_setosa['SW']))
print(np.mean(iris_versicolor['SW']))
print(np.mean(iris_virginica['SW']))

# find median of each class Petal Length
print(np.median(iris_setosa['PL']))
print(np.median(iris_versicolor['PL']))
print(np.median(iris_virginica['PL']))

#find mode of petal length of each class
from scipy import stats
print(stats.mode(iris_setosa['PL']))
print(stats.mode(iris_versicolor['PL']))
print(stats.mode(iris_virginica['PL']))
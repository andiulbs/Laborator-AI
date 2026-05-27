from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes

import numpy as np

x=np.array([[1],[2],[3],[4]])
y=np.array([2,4,6,8])
model = LinearRegression()
model.fit(x,y)
print(model.predict([[5]]))
print(model.predict([[6]]))
print(model.predict([[7]]))

diabetes = load_diabetes()

import pandas as pd
df= pd.DataFrame(diabetes.data,columns=diabetes.feature_names)
df['target'] = diabetes.target
print(df.head())
print(df.describe())
print(df.min())
print(df.max())

import matplot.pyplot as plt
plt.figure(figsize=(8,6))
plt.title('Histograma BMI')
plt.hist(df['bmi'], bins=20)
plt.xlabel('BMI')
plt.ylabel('Freq')
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(df['bmi'], df["target"],df["age"],cmap="viridis")
plt.xlabel('BMI')
plt.ylabel('Varsta')
plt.title('Creati graficul pentru BMI și vârstă în funcție de variabila țintă.')







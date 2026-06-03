import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

diabetes = load_diabetes()

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target

print(df.head())
print(diabetes.feature_names)
print(df.describe())

plt.figure(figsize=(8, 5))
plt.title('Histograma BMI')
plt.hist(df['bmi'], bins=20, edgecolor='black')
plt.xlabel('BMI')
plt.ylabel('Freq')
plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.scatter(df['bmi'], df['target'], color='blue', alpha=0.6)
ax1.set_xlabel('BMI')
ax1.set_ylabel('Target (Progresia bolii)')
ax1.set_title('Target vs BMI')

ax2.scatter(df['age'], df['target'], color='green', alpha=0.6)
ax2.set_xlabel('varsta')
ax2.set_ylabel('target')
ax2.set_title('target vs varsta')

plt.tight_layout()
plt.show()

X_simplu = df[['bmi']]
y = df['target']

X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X_simplu, y, test_size=0.2, random_state=42)

model_simplu = LinearRegression()
model_simplu.fit(X_train_s, y_train_s)

y_pred_s = model_simplu.predict(X_test_s)

plt.figure(figsize=(8, 5))
plt.scatter(X_test_s, y_test_s, color='blue', label='Date Reale')
plt.plot(X_test_s, y_pred_s, color='red', linewidth=2, label='Linia de Regresie')
plt.xlabel('BMI')
plt.ylabel('Target (Progresia bolii)')
plt.title('Regresie Liniara: Predictia progresiei in functie de BMI')
plt.legend()
plt.show()

mse = mean_squared_error(y_test_s, y_pred_s)
print(f"Eroarea opatratica medie: {mse:.2f}")

X_multi = df[['bmi', 'bp']]

X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(X_multi, y, test_size=0.2, random_state=42)

model_multi = LinearRegression()
model_multi.fit(X_train_m, y_train_m)

print(f"Pentru BMI: {model_multi.coef_[0]:.2f}")
print(f"Pentru BP: {model_multi.coef_[1]:.2f}")

y_pred_m = model_multi.predict(X_test_m)
scor_r2 = r2_score(y_test_m, y_pred_m)
print(f"Scorul R^2: {scor_r2:.4f}")
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


iris = load_iris()
X = iris.data
y = iris.target

print("--- 1. Explorare date ---")
print(f"Număr de exemple și caracteristici (shape): {X.shape}")
print(f"Denumirile caracteristicilor: {iris.feature_names}")
print(f"Numele claselor: {iris.target_names}")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\n--- 2. Împărțire date ---")
print(f"Formă set antrenament (X_train): {X_train.shape}")
print(f"Formă set testare (X_test): {X_test.shape}")


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\n--- 3. Preprocesare ---")
print("Primele 3 exemple ÎNAINTE de scalare:\n", X_train[:3])
print("Primele 3 exemple DUPĂ scalare:\n", X_train_scaled[:3])


knn = KNeighborsClassifier(n_neighbors=3)


knn.fit(X_train_scaled, y_train)
y_pred = knn.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

print("\n--- 4. Antrenare model ---")
print(f"Acuratețea pe setul de testare (k=3): {accuracy * 100:.2f}%")

print("\n--- 5. Impactul valorii k ---")
acurateti = []
valori_k = range(1, 16)


for k in valori_k:
    knn_temp = KNeighborsClassifier(n_neighbors=k)
    knn_temp.fit(X_train_scaled, y_train)
    scor = knn_temp.score(X_test_scaled, y_test)
    acurateti.append(scor)


plt.figure(figsize=(8, 5))
plt.plot(valori_k, acurateti, marker='o', linestyle='dashed', color='b')
plt.title('Acuratețea modelului în funcție de k')
plt.xlabel('Valoarea k')
plt.ylabel('Acuratețe pe setul de testare')
plt.xticks(valori_k)
plt.grid(True)
plt.show()
print("\n--- 6. Evaluare detaliată ---")
print("Matricea de confuzie:\n", confusion_matrix(y_test, y_pred))
print("\nRaport de clasificare:\n", classification_report(y_test, y_pred, target_names=iris.target_names))

print("\n--- 7. Vizualizare și Predicție ---")

plt.figure(figsize=(8, 5))
scatter = plt.scatter(X[:, 2], X[:, 3], c=y, cmap='viridis', edgecolor='k')
plt.xlabel(iris.feature_names[2])  # Petal length
plt.ylabel(iris.feature_names[3])  # Petal width
plt.title('Distribuția claselor Iris pe baza petalelor')

handles, _ = scatter.legend_elements()
plt.legend(handles, iris.target_names, title="Clase")
plt.show()

try:
    print("\nIntroduceți datele pentru o nouă floare:")
    sepal_l = float(input("Lungime sepală (ex: 5.1): "))
    sepal_w = float(input("Lățime sepală (ex: 3.5): "))
    petal_l = float(input("Lungime petală (ex: 1.4): "))
    petal_w = float(input("Lățime petală (ex: 0.2): "))

    floare_noua = np.array([[sepal_l, sepal_w, petal_l, petal_w]])
    floare_noua_scaled = scaler.transform(floare_noua)
    pred_idx = knn.predict(floare_noua_scaled)[0]
    nume_clasa = iris.target_names[pred_idx]

    print(f"\n=>  Modelul KNN a clasificat această floare ca fiind: **{nume_clasa}**")
except ValueError:
    print("doar numere valide!")


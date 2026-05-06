# Exercitii

import pandas as pd
data=pd.read_csv('data.csv')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(data.head(3))

# ex2
print(data[data['Age']>40].head(10))

# ex3
rezultat = data[(data['Overall'] >= 85) & (data['Age'] < 25)]
print(rezultat)

# ex4
# sort=data.sort_values(by=['Skill Moves'], ascending=False)
# print(sort)

# ex5
# contr = data[data['Contract Valid Until'] == 2021]
# print(contr)

# ex6
print("Randuri:", data.shape[0])
print("Coloane:", data.shape[1])

print('jucatori unici:',data['Name'].nunique())

#ex7
freq = data['Nationality'].value_counts().head(5)
print(freq)

#ex8
plt.figure(figsize=(8,6))
plt.pie(top5=freq)


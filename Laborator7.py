import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")


# ex 1
print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())


# ex 2
categorical_vars = df.select_dtypes(include=['object']).columns.tolist()
numeric_vars = df.select_dtypes(exclude=['object']).columns.tolist()

print("Variabile categorice:", categorical_vars)
print("Variabile numerice:", numeric_vars)

# ex 3


for col in numeric_vars:
    df[col].fillna(df[col].median(), inplace=True)

for col in categorical_vars:
    df[col].fillna("Unknown", inplace=True)


print(df.isnull().sum())


# ex 4

from sklearn.preprocessing import LabelEncoder


le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])

df = pd.get_dummies(df, columns=['race/ethnicity',
                                 'parental level of education',
                                 'lunch',
                                 'test preparation course'],
                    drop_first=True)

print(df.head())

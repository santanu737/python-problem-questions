# case study - titanic dataset (kaggle)

import pandas as pd

# importing the titanic csv file downloaded from kaggle (saved as train.csv)
df=pd.read_csv("train.csv")
print(df.head())
print("\nColumns:", list(df.columns))

# 1. cleaning the dataset
# checking which columns have null values
print("\nNull values in each column:")
print(df.isnull().sum())

# age has some nulls, so filling them with the median age
df['Age'] = df['Age'].fillna(df['Age'].median())

# embarked has only 2 nulls, so filling with the most common port
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# cabin has too many nulls, so dropping the whole column
df = df.drop(columns=['Cabin'])

print("\nCleaned dataset:")
print(df)

# 2. details of female passengers whose age is more than 40
female_above_40 = df[(df['Age'] > 40) & (df['Sex'] == 'female')]
print("\nFemale passengers above 40:")
print(female_above_40)

# 3. describe the dataset for passengers of class 1
class1 = df[df['Pclass'] == 1]
print("\nDescribe for class 1 passengers:")
print(class1.describe())

# 4. removing duplicate passenger ids (if any)
print("\nDuplicates before:", df.duplicated(subset=['PassengerId']).sum())
df = df.drop_duplicates(subset=['PassengerId'])
print("Duplicates after:", df.duplicated(subset=['PassengerId']).sum())

# 5. inserting a new column (family size = siblings/spouse + parents/children + self)
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
print("\nDataset with new column:")
print(df.head())
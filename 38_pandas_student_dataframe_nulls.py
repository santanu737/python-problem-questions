# Q4. create the student dataframe with roll, name, dept and marks
# find null columns, fill sima's null with CSE, delete binita's null row
# update raju's dept to NIST

import pandas as pd

data = {
"roll": [1,2, 3,4, 5],
"name":["Anu", "Ria","Sima", "Raju","Binita"],
"dept": ["ESE","IT", None,"ESE", None],
"marks":[90, None,80, 85,95]
}
df = pd.DataFrame(data)
print(df)

# columns with null values
print(df.isnull().sum())

# filling sima's null dept with cse
df.loc[df['name']=='Sima', 'dept']= df.loc[df['name'] == 'Sima', 'dept'].fillna("CSE")

# deleting binita's null row
df= df.dropna(subset=['dept'])

# updating raju's dept
df.loc[df['name'] =='Raju', 'dept']= "NIST"

print(df)
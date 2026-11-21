#  Create a dataframe with emp_id, emp_name, contact_no, project_location
# (one employee may have more than one contact no, project location may be more than one).
# Take 5 employees in wide format where the contact no depends on project location.
# Then reshape the table to long format using melt() method.

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "emp_id":[101,102,103,104,105],
    "emp_name":["Amit","Riya","Santanu","Neha","Rahul"],
    "contact_Kolkata" : ["9830011111","9830022222","9830033333",np.nan,"9830055555"],
    "contact_Mumbai":["9820011111",np.nan,"9820033333","9820044444",np.nan],
    "contact_Delhi" :[np.nan,"9810022222",np.nan,np.nan,"9810055555"],
    "contact_Bangalore":[np.nan,np.nan,"9845033333","9845044444",np.nan]
})

print("wide format")
print(df)
print("shape :",df.shape)

df2 = pd.melt(df,id_vars=["emp_id","emp_name"],var_name="project_location",value_name = "contact_no")

print("\nafter melt")
print(df2)

df2["project_location"] = df2["project_location"].str.replace("contact_","")
df2 = df2.dropna()
df2 = df2.sort_values("emp_id").reset_index(drop=True)

print("\nlong format")
print(df2)
print("shape :",df2.shape)

print("\ncount of contacts per emp")
print(df2.groupby("emp_name")["contact_no"].count())
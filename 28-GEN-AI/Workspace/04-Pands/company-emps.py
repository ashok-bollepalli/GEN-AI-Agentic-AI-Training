import pandas as pd

employees = {
    "EmpId": [101, 102, 103, 104, 105, 106],
    "Name": ["Ravi", "Sita", "Kiran", "Rahul", "Priya", "Anil"],
    "Department": ["IT", "HR", "IT", "Sales", "HR", "IT"],
    "Salary": [50000, 45000, 70000, 40000, 48000, 65000],
    "Experience": [2, 5, 8, 1, 4, 7]
}

df = pd.DataFrame(employees)
print(df)
print("---------------------------------------------")
print(df.head(3))
print("---------------------------------------------")
print(df.tail(3))
print("---------------------------------------------")
print(df["Name"])
print("---------------------------------------------")
print(df[["Name", "Salary"]])

print("---------------------------------------------")

print(df[df["Salary"] > 50000])

print("---------------------------------------------")

print(df[df["Department"] == "IT"])

print("---------------------------------------------")

print(df[(df["Department"] == "IT") & (df["Salary"] > 60000)])

print("---------------------------------------------")

print(df[(df["Department"] == "IT") | (df["Salary"] > 60000)])

print("---------------------------------------------")

print(df.sort_values("Salary"))

print(df.sort_values("Salary", ascending=False))

print(df.sort_values(["Department", "Salary"]))

print("---------------------------------------------")

df["Bonus"] = df["Salary"] * 0.10

print(df)

print("---------------------------------------------")

df["Total Salary"] = df["Salary"] + df["Bonus"]

print(df)

print("---------------------------------------------")

df.drop(columns=["Bonus"], inplace=True)
print(df)

print("---------------------------------------------")

print(df.groupby("Department")["Salary"].mean())
print(df.groupby("Department")["Salary"].max())
print(df.groupby("Department")["Salary"].min())
print(df.groupby("Department")["Salary"].sum())

print("---------------------------------------------")

print(df["Department"].unique())
print(df["Department"].nunique())

print("---------------------------------------------")

emps = {
    "Name":["Ravi","Sita","Kiran","Rahul"],
    "Salary":[50000,None,65000,None]
}

ndf = pd.DataFrame(emps)

print(ndf)
#print(df.isnull())
print("---------------------------------------------")

ndf["Salary"] = ndf["Salary"].fillna(0)
print(ndf)
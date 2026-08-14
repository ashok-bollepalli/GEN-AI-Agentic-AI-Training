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
print(df.head(3))
print(df.tail(3))
print(df["Name"])
print(df[["Name", "Salary"]])
print(df[df["Salary"] > 50000])
print(df[df["Department"] == "IT"])

print(df[(df["Department"] == "IT") & (df["Salary"] > 60000)])

print(df.sort_values("Salary"))
print(df.sort_values("Salary", ascending=False))
print(df.sort_values(["Department", "Salary"]))

df["Bonus"] = df["Salary"] * 0.10
print(df)

df["Total Salary"] = df["Salary"] + df["Bonus"]
print(df)

df.drop(columns=["Salary", "Bonus"], inplace=True)
print(df)

print(df.groupby("Department")["Total Salary"].min())
print(df.groupby("Department")["Total Salary"].max())
print(df.groupby("Department")["Total Salary"].sum())
print(df.groupby("Department")["Total Salary"].mean())


print(df["Department"].unique())
print(df["Department"].nunique())

print("---------------------------------------------")

emps = {
    "Name":["Ravi","Sita","Kiran","Rahul","Ashok", "Ashok"],
    "Salary":[50000,None,65000,None, 25000, 25000]
}
df = pd.DataFrame(emps)
print(df)

# Check Duplicate records
print(df.duplicated().sum())

df = df.drop_duplicates()

print(df)
print("-----------------------------")
df["Salary"] = df["Salary"].fillna(0)
print(df)
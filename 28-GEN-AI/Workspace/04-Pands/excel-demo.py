import pandas as pd

students = {
    "name": ["Ravi", "Sita", "Kiran"],
    "course": ["Python", "Java", "DevOps"],
    "marks": [80, 90, None]
}

df = pd.DataFrame(students)
df.to_excel("Students.xlsx", index=False)

print("----------Excel Created Successfully----------")

df = pd.read_excel("Students.xlsx")
print(df)
print("-------------------")

print(df.head(1))

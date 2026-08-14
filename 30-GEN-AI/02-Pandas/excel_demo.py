import pandas as pd

students = {
    "name": ["Ravi", "Sita", "Kiran"],
    "course": ["Python", "Java", "DevOps"],
    "marks": [80, 90, 75]
}

df = pd.DataFrame(students)
print(df)

df.to_excel("students.xlsx", index=False)

print("----------Excel Created Successfully----------")

df = pd.read_excel("students.xlsx")
print(df)
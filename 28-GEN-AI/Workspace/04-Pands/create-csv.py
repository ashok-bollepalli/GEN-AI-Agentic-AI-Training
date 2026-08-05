import pandas as pd

students = {
    "name": ["Ravi", "Sita", "Kiran"],
    "course": ["Python", "Java", "DevOps"],
    "marks": [80, 90, 75]
}

df = pd.DataFrame(students)

df.to_csv("students.csv", index=False)

print("CSV file created successfully")




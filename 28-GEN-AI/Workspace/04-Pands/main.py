import pandas as pd

marks = pd.Series([10,20,30,40])
print(marks)

#---------------------------------------

print("-------------------------------------")

students = {
    "name": ["Ravi", "Sita", "Kiran"],
    "course": ["Python", "Java", "DevOps"],
    "marks": [80, 90, 75]
}

df = pd.DataFrame(students)
print(df)
print("-------------------------------------")


# Create series with custom index

courses = pd.Series(
    ["Python", "JAVA", "DevOps"],
    index = ["C1", "C2", "C3"]
)

print(courses)
print(courses["C1"])

courses.to_csv("data.csv")



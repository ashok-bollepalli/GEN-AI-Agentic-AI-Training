import pandas as pd

marks = pd.Series([10, 20, 30, 40])
print(marks)

marks = pd.Series(
          [10, 20, 30, 40, 50],
          index = ["SB-1", "SB-2", "SB-3", "SB-4", "SB-5"]
        )
print(marks)


courses = pd.Series(
    ["Python", "JAVA", "DevOps"],
    index = ["C1", "C2", "C3"]
)

print(courses)
print(courses["C1"])



students = {
    "name": ["Ravi", "Sita", "Kiran"],
    "course": ["Python", "Java", "DevOps"],
    "marks": [80, 90, 75]
}
df = pd.DataFrame(students)
print(df)

print(df.head())
print(df.head(2))
print(df.tail())
print(df.tail(2))

print(df.info())
print(df.describe())








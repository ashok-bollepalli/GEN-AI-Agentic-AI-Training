import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

sql = "select * from students"

cursor.execute(sql)

students = cursor.fetchall()
print(type(students))

for student in students:
    print(student)

connection.close()
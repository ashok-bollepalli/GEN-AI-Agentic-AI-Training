import sqlite3
connection = sqlite3.connect("students.db")
cursor = connection.cursor()

sql = "select * from students where student_id = ?"

student_id = input("Enter student id: ")

cursor.execute(sql, (student_id,))

student = cursor.fetchone()

print(student)

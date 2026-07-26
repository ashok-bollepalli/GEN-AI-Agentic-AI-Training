import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

student_name = input("Enter student name: ")
student_email = input("Enter student email: ")
student_course = input("Enter student course: ")
student_fee = input("Enter student feed: ")

sql = """insert into students(
    student_name, 
    student_email, 
    student_course, 
    student_fee) values (?,?,?,?)
"""

cursor.execute(sql, (student_name,
                     student_email,
                     student_course,
                     student_fee)
                )

print("Student inserted successfully")

connection.commit()
connection.close()
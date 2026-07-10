import sqlite3

# Establish DB connection
connection = sqlite3.connect("students.db")

# Create cursor object to execute SQL queries
cursor = connection.cursor()

student_name = input("Enter Student Name: ")
student_email = input("Enter Student Email: ")
student_course = input("Enter Course Name: ")
student_fee = float(input("Enter Course Fee: "))

cursor.execute(""" INSERT INTO students (student_name, student_email, student_course, student_fee) 
                   VALUES (?, ?, ?, ?) """,(student_name, student_email, student_course, student_fee))

connection.commit()
print("Student inserted successfully")
connection.close()

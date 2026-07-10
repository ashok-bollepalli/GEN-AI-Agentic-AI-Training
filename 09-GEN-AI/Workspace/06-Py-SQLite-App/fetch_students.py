import sqlite3

# Establish DB connection
connection = sqlite3.connect("students.db")

# Create cursor object to execute SQL queries
cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)

connection.close()

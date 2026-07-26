import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

sql = """
create table if not exists students (
    student_id integer primary key autoincrement,
    student_name text not null,
    student_email text not null,
    student_course text not null,
    student_fee integer not null)
"""

cursor.execute(sql)

print("Students table created successfully")

connection.commit()
connection.close()
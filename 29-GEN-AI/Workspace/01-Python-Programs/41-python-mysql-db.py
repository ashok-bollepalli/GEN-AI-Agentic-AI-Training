import mysql.connector

connection = mysql.connector.connect(
                        host = "localhost",
                        port=3306,
                        user = "root",
                        passwd = "root",
                        database = "pydb"
                )
cursor = connection.cursor()


sql = """
create table if not exists students (
    student_id INT primary key auto_increment,
    student_name VARCHAR(100) not null,
    student_email VARCHAR(100) not null,
    student_course VARCHAR(100) not null,
    student_fee INT not null)
"""

cursor.execute(sql)

print("Students table created successfully")

connection.commit()
connection.close()
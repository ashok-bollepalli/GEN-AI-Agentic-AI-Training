import mysql.connector

connection = mysql.connector.connect(
                        host = "localhost",
                        port=3306,
                        user = "root",
                        passwd = "root",
                        database = "pydb"
                )

cursor = connection.cursor()

sql = "select * from students"

cursor.execute(sql)

students = cursor.fetchall()

for student in students:
    print(student)

connection.close()
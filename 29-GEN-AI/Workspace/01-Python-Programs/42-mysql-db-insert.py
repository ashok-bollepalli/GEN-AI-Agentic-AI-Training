import mysql.connector

connection = mysql.connector.connect(
                        host = "localhost",
                        port=3306,
                        user = "root",
                        passwd = "root",
                        database = "pydb"
                )

cursor = connection.cursor()

student_name = input("Enter student name: ")
student_email = input("Enter student email: ")
student_course = input("Enter student course: ")
student_fee = input("Enter student fee: ")

sql = """insert into students(student_name,
                              student_email,
                              student_course,
                              student_fee)
         values (%s, %s, %s, %s)
      """

values = (
    student_name,
    student_email,
    student_course,
    student_fee
)

cursor.execute(sql, values)

print("Student inserted successfully")

connection.commit()
connection.close()
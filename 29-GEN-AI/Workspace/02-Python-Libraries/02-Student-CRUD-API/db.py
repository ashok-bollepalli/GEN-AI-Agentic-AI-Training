import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="pydb"
    )

def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS STUDENTS(
            ID INT AUTO_INCREMENT PRIMARY KEY,
            NAME VARCHAR(100) NOT NULL,
            COURSE VARCHAR(100) NOT NULL,
            FEE DECIMAL(10,2) NOT NULL
        )
    """

    cursor.execute(query)
    cursor.close()
    connection.commit()
    connection.close()
    print("Table created successfully...")

def insert_student(student):
    connection = get_connection()
    cursor = connection.cursor()

    query = "insert into students(name, course, fee) values (%s, %s, %s)"

    cursor.execute(query, (student.name, student.course, student.fee))

    connection.commit()
    cursor.close()
    connection.close()

    return {
        "success": True,
        "message": "Student created!",
        "data": student
    }

def get_students():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = "select * from students"

    cursor.execute(query)
    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return {
        "success": True,
        "message" : "Student fetched successfully !!",
        "data": students
    }

def get_student_by_id(id):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    query = "select * from students where id = %s"
    cursor.execute(query, (id,))
    student = cursor.fetchone()
    cursor.close()
    connection.close()
    return {
        "success": True,
        "message" : "Student fetched successfully !!",
        "data": student
    }

def delete_student_by_id(id):
    connection = get_connection()
    cursor = connection.cursor()
    query = "delete from students where id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    cursor.close()
    connection.close()
    return {
        "success": True,
        "message" : "Student deleted successfully !!"
    }

def update_student(id, student):
    connection = get_connection()
    cursor = connection.cursor()
    query = "update students set name = %s, course = %s, fee = %s where id = %s"
    cursor.execute(query, (student.name, student.course, student.fee, id))
    connection.commit()
    cursor.close()
    connection.close()
    return {
        "success": True,
        "message" : "Student updated successfully !!",
    }






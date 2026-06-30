import sys

a = 20
print(a)
print(type(a))
print("size of a var in bytes", sys.getsizeof(a))

my_name = "Ashok"
print(my_name)
print(type(my_name))
print("size of my_name var in bytes", sys.getsizeof(my_name))


# Flot Data Type
price = 99.99
percentage = 85.5

print(price, type(price))
print("size of price : ", sys.getsizeof(price))
print(percentage, type(percentage))
print("size of percentage : ", sys.getsizeof(percentage))

# list data type (ordered + mutable + duplicates allowed)
students = ["Anil", "Sunil", "Gopi", "Anil"]
print(students)
print(type(students))
print("size of students : ", sys.getsizeof(students))

# tuple data type (ordered + Immutable + Duplicates allowed)
courses = ("Java", "Python", "GEN AI", "Python")
print(courses)
print(type(courses))

# set data type (Un Ordered + Mutable + No Duplicates)
skills = {"Java", "Python", "GEN AI", "DevOps", "Cloud", "Java"}
print(skills)
print(type(skills))

# dictionary data type (key-value pair)
student  = {
    "id" : 101,
    "name" : "Ashok",
    "gender" : "Male"
}
print(student)
print(type(student))


# Student Data
student_id = 101
student_name = "John"
course = "Python"
fee = 5000.00
is_paid = True
imp_concepts  = ["Fundamentals", "Variables", "DSA", "OOPS"]
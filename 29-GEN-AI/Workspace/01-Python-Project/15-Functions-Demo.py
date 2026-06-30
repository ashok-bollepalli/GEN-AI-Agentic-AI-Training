# creating function
def greet():
    print("Hello World")

# call the function
greet()

# function with parameter
def wish(name):
    print(name, " Welcome to Ashok IT...")

# call the function by passing argument
wish("Ashok")
wish("John")
wish("Smith")

# function with multiple parameters
def print_student_data(name, course):
    print("Student Name is :", name)
    print("Student Course is :", course)

print_student_data("John", "Python")


# function with parameters and return value
def add(a, b):
    return a + b
    print("Execution completed")

result = add(10,20)
print("The result is :", result)


# function
def login():
    pass
print("Completed")

def student(name="Raj", course="GEN AI"):
    print("Name:", name)
    print("Course:", course)

student("Ashok", "Python")
student(course="GEN AI", name="John")
student(name="Smith")
student()


# function with variable arguments

def print_numbers(*i):
    print(i)

print_numbers(10)
print_numbers(10,20)
print_numbers(10,20,30)

# perform sum of numbers using variable length args
def add_numbers(*nums):
    total = 0
    for num in nums:
        total = total + num
    return total

print(add_numbers(10,20))
print(add_numbers(10,20,30))
print(add_numbers(10,20,30,40))

# function with keyword variable length args

def student_info(**args):
    print(args)

student_info(name="Raj", course="GEN AI")
student_info(name="Ram", course="GEN AI", fee=10000)
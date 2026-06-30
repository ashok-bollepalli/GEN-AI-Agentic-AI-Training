a = 10
b = 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.3333 (quotient)
print(a // b)  # Floor Division: 3 (quotient without decimal)
print(a % b)   # Modulus / Remainder: 1

# additional assignment
balance = 1000
deposit_amount = 200
# balance = balance + deposit_amount
balance += deposit_amount
print(balance)


withdraw_amount = 200
#balance  = balance - withdraw_amount
balance -= withdraw_amount
print(balance)

## Comparison operators are used to compare two values. They return True or False.
a = 10
b = 20

print(a == b)   # Equal to: False
print(a != b)   # Not equal to: True
print(a > b)    # Greater than: False
print(a < b)    # Less than: True
print(a >= b)   # Greater than or equal to: False
print(a <= b)   # Less than or equal to: True

## Logical operators are used to combine multiple conditions.
age = 25
salary = 50000

print(age > 18 and salary > 30000) # True bcz both conditions satisfied

print(age > 18 or salary > 40000) # True

print(not age > 35)

## Membership operators are used to check whether a value is available inside a sequence like list, tuple, string, etc.
students = ["Ashok", "Ramesh", "Suresh"]

print("Ashok" in students)       # True
print("Kiran" in students)       # False

## Identity operators are used to compare memory location of objects.
a = 20
b = 20
print(a is b)
print(a is not b)

print(id(a))
print(id(b))
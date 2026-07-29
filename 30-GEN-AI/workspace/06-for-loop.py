# range(stop)
for i in range(6):
    print(i)

# range(start, stop)
for i in range(1, 6):
    print(i)

# range(start, stop, step)
for i in range(1, 11, 2):
    print(i)

# for loop with string
name = "Ashok"
for ch in name:
    print(ch)

# for loop with List
students = ["Ashok", "Ram", "John"]
for stu in students:
    print(stu)

# for loop with Tuple
courses = ("JAVA", "Python", "AI")
for course in courses:
    print(course)

# for loop with Set
places = {"Hyd", "Banglore", "Pune"}
for place in places:
    print(place)


#for loop with dictionary
student = {
    "id" : 101,
    "name" : "Ashok",
    "gender" : "Male"
}

for key in student:
    print(key, "-->", student[key])


# cart prices for items

cart_prices = [100, 200, 150]
total = 0

for a in cart_prices:
    total = total + a

print(total)
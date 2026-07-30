student = {
    "name": "Ravi",
    "age": 25,
    "course": "Python",
    "marks": 85
}

print(student)
print(student["name"])
#print(student["gender"])
print(student.get("gender"))

print(student.keys())
print(student.values())
print(student.items())

student.update({"name" : "Ashok"})
print(student)

# pop() removes item based on key.
student.pop("marks")
print(student)

for key, value in student.items():
    print(value)

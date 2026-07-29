# --------------------------------- #

import json

student = {
    "id": 101,
    "name": "Ravi",
    "course": "Python",
    "fee": 15000
}
print(type(student))

student_json = json.dumps(student)
print(student_json)

print(type(student_json))

#--------------------------------#

with open("student.json", "w") as file:
    json.dump(student, file)

print("JSON file created successfully")

#--------------------------------#

student = json.loads(student_json)
print(student)
print(type(student))

#--------------------------------#

with open("student.json", "r") as file:
    student = json.load(file)
    print(student)

#--------------------------------#

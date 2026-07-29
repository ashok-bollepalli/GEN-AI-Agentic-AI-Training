for i in range(1, 11):
    if i== 5:
        break
    print(i)

#------------------------#
print("-----------------------")

for i in range(1, 11):
    if i== 5:
        continue
    print(i)
#-----------------------------#

students = [
    {"name": "Ravi", "marks": 80},
    {"name": "Kiran", "marks": 30},
    {"name": "Sita", "marks": 90}
]

for s in students:
    if s["marks"] < 35:
        continue
    print("Certificate sent for : ", s["name"])
age  = int(input("Enter your Age : "))

if age > 18:
    print("Eligible")
    print("Give vote to right person")
else:
    print("Not eligible for vote")

########################################################

marks = int(input("Enter your marks : "))

if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 65:
    print("C Grade")
elif marks >= 35:
    print("Just Pass")
else:
    print("Failed")

#---------------------------------------#

print("1. Add Student")
print("2. View Student")
print("3. Update Student")
print("4. Delete Student")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Student added")
    case 2:
        print("Fetched Students")
    case 3:
        print("Student Updated")
    case 4:
        print("Student Deleted")
    case _:
        print("Invalid Choice selected")
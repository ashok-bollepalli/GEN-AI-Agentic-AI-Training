courses = ("JAVA", "Python", "GEN AI", "DEVOPS", ".Net", "MERN")
print(courses)
print(type(courses))

print(courses[0])
print(courses[1:3])

print(courses.index("GEN AI"))

print(len(courses))

sorted_courses = sorted(courses)
print(sorted_courses)

numbers = (10, 15, 30, 20, 40, 25)

print(numbers)

numbers_list = list(numbers)
print(numbers_list)

courses = ("JAVA", "Python", "GEN AI", "DEVOPS", ".Net", "MERN")

del courses

numbers = (10, 15, 30, 20, 40, 25)
print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))

for n in numbers:
    print(n)

# list creation
courses = ["JAVA", "Python", "DevOps", "GEN AI", ".NET"]

print(courses)

# Positive Indexing (starts from left to right)
print(courses[0])
print(courses[1])

#negative index (starts from right to left)
print(courses[-1])

# Slicing : used to get a part of list
print(courses[1:3])
print(courses[2:])
print(courses[:3])
print(courses[::2])
print(courses[::-1])


### List Functions ####
# append : append() adds an element at the end of the list
# insert : insert() adds an element at specified index
# extends : extend() adds multiple elements to the list.
# remove : remove() removes the specified value
# pop : pop() removes element based on index. If index is not given, pop() removes the last element
# index : index() to identify index position of given element
# clear : clear() removes all elements from the list.
# del : del can delete an element or entire list.
# sort : Sort the list elements in asc/dsc

courses = ["PYTHON", "JAVA"]
courses.append("DEVOPS")
print(courses)

courses.insert(1, "GEN AI")
print(courses)

frontend = ["HTML", "CSS"]
backend = ["Python", "Django"]
frontend.extend(backend)
print(frontend)


frontend.remove("CSS")
print(frontend)

frontend.pop()
print(frontend)

frontend.clear()
print(frontend)

del frontend
#print(frontend)


courses = ["JAVA", "Python", "DevOps", "GEN AI", ".NET"]

for course in courses:
    print(course, "--", courses.index(course))

index = courses.index("GEN AI")
print(index)

numbers = [1, 3, 6, 9, 2]
print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)




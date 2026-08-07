import matplotlib.pyplot as plt

courses = ["Python", "Java", "DevOps", "AWS"]
students = [50, 40, 30, 35]

#plt.bar(courses, students)
plt.barh(courses, students)

plt.title("Course Enrollment Report")
plt.xlabel("Course")
plt.ylabel("Students Count")

plt.show()
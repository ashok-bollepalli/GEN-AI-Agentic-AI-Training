import matplotlib.pyplot

students = ["Ravi", "Anil", "Priya", "Sneha"]
marks = [75, 85, 90, 80]

matplotlib.pyplot.bar(students, marks)

matplotlib.pyplot.title("Student Marks")
matplotlib.pyplot.xlabel("Student Names")
matplotlib.pyplot.ylabel("Marks")

matplotlib.pyplot.show()
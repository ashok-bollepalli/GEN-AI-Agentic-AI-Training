import matplotlib.pyplot as plt

marks = [35, 45, 50, 60, 65, 70, 75, 80, 85, 90, 95]

plt.hist(marks)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()
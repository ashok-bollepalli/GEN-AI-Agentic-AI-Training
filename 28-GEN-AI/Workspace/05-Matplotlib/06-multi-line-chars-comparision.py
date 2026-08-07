import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]

python_sales = [10000, 15000, 12000, 18000]
java_sales = [8000, 12000, 10000, 14000]

plt.plot(months, python_sales, marker="o", label="Python")
plt.plot(months, java_sales, marker="o", label="Java")

plt.title("Course Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.legend()

plt.grid()

plt.show()
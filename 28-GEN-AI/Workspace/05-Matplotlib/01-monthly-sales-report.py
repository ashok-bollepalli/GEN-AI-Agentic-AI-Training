import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [10000, 15000, 12000, 18000]

plt.plot(months, sales, marker="o", linestyle="--", color="blue")

plt.title("Sales by Month")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

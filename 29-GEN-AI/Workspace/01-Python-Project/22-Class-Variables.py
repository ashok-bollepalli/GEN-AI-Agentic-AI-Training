class Student:

    inst_name = "Ashok IT"

    def __init__(self, i, j = "AshokIT"):
        self.name = i
        self.inst_name = j

    def display(self):
        print(self.name, "--", Student.inst_name)

    @staticmethod
    def test():
        print("test")

s1 = Student("Ashok")
s1.display()

s2 = Student("Ram")
s2.display()

Student.test()
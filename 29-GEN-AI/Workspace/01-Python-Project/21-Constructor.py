class Student:

    def __init__(self, a, b, c, d):
        self.id = a
        self.name = b
        self.course = c
        self.marks = d

    def display_result(self):
       if self.marks > 35:
           print(self.name, "Passed")
       else:
           print(self.name, "Failed")

s1 = Student(101, "Ashok", "Python", 45)
s1.display_result()

s2 = Student(102, "Ram", "JAVA", 25)
s2.display_result()




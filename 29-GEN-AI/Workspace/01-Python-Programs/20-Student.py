class Student:
    id = 20
    name = "Ashok"
    def talk(self):
        print(hash(self))
        print("Hi, My Id is :", self.id)
        print("My Name is :", self.name)

# Obj creation
s1 = Student()
s1.talk()

s2 = Student()
s2.talk()

print(hash(s1))
print(hash(s2))
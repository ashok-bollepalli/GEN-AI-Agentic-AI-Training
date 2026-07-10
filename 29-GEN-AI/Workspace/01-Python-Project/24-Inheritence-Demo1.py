class Parent:
    def house(self):
        print("Parents House")

class Child(Parent):
    def bike(self):
        print("Child Bike")

c  = Child()
c.house()
c.bike()
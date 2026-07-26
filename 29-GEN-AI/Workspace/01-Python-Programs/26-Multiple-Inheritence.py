class Father:
    def father_property(self):
        print("Accessing Father Property")
    def m1(self):
        print("Father m1() called...")
#----------------------------------------------------#

class Mother:
    def mother_property(self):
        print("Accessing Mother Property")
    def m1(self):
        print("Mother m1() called...")
#----------------------------------------------------#
class Child(Mother, Father):
    def child_property(self):
        print("Accessing Child Property")

obj = Child()
obj.father_property()
obj.mother_property()
obj.child_property()
obj.m1()
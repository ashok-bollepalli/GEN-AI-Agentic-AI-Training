class Parent:
    def cash(self):
        print("Parents cash.....")
    def bike(self):
        print("Parent bike (Splender).....")

class Child(Parent):
    def bike(self):
        super().bike()
        print("Child bike (Royal Enfiled).....")

obj = Child()
obj.bike()

#########################

class Calculator:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c

calc = Calculator()
print(calc.add(10,20,30))
print(calc.add(1,2))
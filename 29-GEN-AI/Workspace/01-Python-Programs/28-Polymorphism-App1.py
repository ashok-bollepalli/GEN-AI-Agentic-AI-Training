class Dog:
    def sound(self):
        print("Dog Barks...")

class Cat:
    def sound(self):
        print("Cat Meow...")

##################################
def animal_sound(animal):
    animal.sound()
#################################

dog = Dog()
cat = Cat()

animal_sound(cat)

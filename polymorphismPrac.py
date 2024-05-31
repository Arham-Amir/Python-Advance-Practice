class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

class Tortise(Animal):
    pass

animals = [Dog(), Cat(), Tortise()]
for animal in animals:
    animal.speak()

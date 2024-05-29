class Animal:
    def speak(self):
        print('Animal Speaks')

class Dog(Animal):
    def speak(self):
        print("Dog Speaks")
    
class Cat(Animal):
    def speak(self):
        print("Cat Speaks")

class Mix(Dog, Cat):
    pass

a1 = Animal()
a1.speak()

a2 = Dog()
a2.speak()

a3 = Cat()
a3.speak()

a4 = Mix()
a4.speak()
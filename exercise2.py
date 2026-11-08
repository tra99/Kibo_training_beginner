
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    # Override
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

dog=Dog()
cat=Cat()

animals=[dog, cat]

for ani in animals:
    ani.speak()

class Animal:
    def speak(self):
        print("...")


class Dog(Animal):
    def speak(self):
        print("Woof")  


my_dog = Dog()


my_dog.speak()
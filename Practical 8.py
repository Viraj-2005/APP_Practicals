class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Unknown sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

if __name__ == "__main__":
    animal = Animal("Generic Animal")
    print(animal.name)   # Output: Generic Animal
    print(animal.speak())  # Output: Unknown sound

    dog = Dog("Buddy")
    print(dog.name)      # Output: Buddy
    print(dog.speak())   # Output: Woof!

    cat = Cat("Whiskers")
    print(cat.name)      # Output: Whiskers
    print(cat.speak())   # Output: Meow!

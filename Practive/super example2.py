"""เรียก __init__() ของคลาสแม่"""

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # เรียก constructor ของ Animal
        self.breed = breed

dog = Dog("Buddy", "Labrador")
print(dog.name)   # Buddy
print(dog.breed)  # Labrador
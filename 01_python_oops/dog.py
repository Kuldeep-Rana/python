from animal import Animal

class Dog(Animal):

    def __init__(self, type, name, age, sound="Bhaw Bhaw"):
        self.sound = sound
        self.age = age
        super().__init__(type, name)        


    def describe(self):
        print(f"{super().getName()} is a {super().getType()}, {self.age} years old and makes {self.sound} sound")

d = Dog("PET", "Tommy", 2)

d.describe()

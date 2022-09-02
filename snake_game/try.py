class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this under water")

    def swim(self):
        print("moving in water")


class Dog:
    def __init__(self):
        self.temperature = "loyal"


class Labrator(Dog):
    def __init__(self):
        super().__init__()
        self.temperature = "gentle"


dog = Dog()
print(f"A dog is {dog.temperature}")

sparky = Labrator()
print(f"Sparky is {sparky.temperature}")

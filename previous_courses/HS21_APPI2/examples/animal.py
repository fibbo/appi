class Animal:
    def __init__(self, weight):
        self.weight = weight

    def info(self):
        print(f"I'm an abstract animal and I don't have a concept of weight.")

    def noise(self):
        print("I'm abstract, I don't make noises. Or maybe abstract noises...")


class Cat(Animal):
    def __init__(self, weight, color):
        super().__init__(weight)
        self.color = color

    def info(self):
        print(f"I'm a {self.color} cat that weights {self.weight} kg.")

    def noise(self):
        print("Meow")


class Dog(Animal):
    def __init__(self, weight, breed):
        super().__init__(weight)
        self.breed = breed

    def info(self):
        print(f"I'm a {self.breed} dog that weights {self.weight} kg.")

    def noise(self):
        print("Woof!")


cat = Cat(6, "Red")

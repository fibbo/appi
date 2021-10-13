class Fruit:
    def eatable(self):
        pass

    def name(self):
        return "Fruit"


class EatableFruit(Fruit):
    def eatable(self):
        return "Yes, I'm eatable"


class NonEatableFruit(Fruit):
    def eatable(self):
        return "You shouldn't eat me"


class Lemon(EatableFruit):
    def name(self):
        return "Lemon"


class Manchineel(NonEatableFruit):
    def name(self):
        return "Manchineel"


fruits = [Lemon(), Manchineel()]

for fruit in fruits:
    print(f"Can I eat {fruit.name()}?: {fruit.eatable()}")

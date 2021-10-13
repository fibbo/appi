class Vet_patient:
    def __init__(self, name, species, breed=None):
        self.name = name
        self.species = species
        self.breed = breed
        self.appointments = []

    def assign_a_new_appontment(self, date_of_appointment):
        self.appointments.append(date_of_appointment)

    def get_appointments(self):
        if self.appointments:
            for i in self.appointments:
                print(i)
        else:
            print("There are no appointments for this patient")

    def make_noise(self):
        print("Abstract doesn't make noises.")


class Dog(Vet_patient):
    def bark(self):
        print("Woof!")

    def make_noise(self):
        self.bark()


class Cat(Vet_patient):
    def Miau(self):
        print("Miau!")

    def make_noise(self):
        self.Miau()


ernie = Dog("Ernie", "Dog", "Labrador")
ernie.bark()
print(ernie.name)
print(ernie.breed)


ernie.assign_a_new_appontment("Friday, 15:40")
ernie.assign_a_new_appontment("Saturday, 16:40")
ernie.get_appointments()


peppi = Cat("Peppi", "cat")
peppi.Miau()
peppi.get_appointments()

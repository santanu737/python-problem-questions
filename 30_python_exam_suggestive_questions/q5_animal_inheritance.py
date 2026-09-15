"""
Question 5:
Define a class Animal with attribute type.
Define a class WildAnimal which is child of Animal with attribute sound, colour.
Define a class PetAnimal which is child of Animal with attribute food, category.
Initialise all variables with constructor.
Create one object of each child class.
Use show() method to display the records of both animals.
"""


class Animal:
    def __init__(self, type_):
        self.type = type_


class WildAnimal(Animal):
    def __init__(self, type_, sound, colour):
        super().__init__(type_)
        self.sound = sound
        self.colour = colour

    def show(self):
        print("Wild Animal Details:")
        print(f"Type   : {self.type}")
        print(f"Sound  : {self.sound}")
        print(f"Colour : {self.colour}")
        print("-" * 30)


class PetAnimal(Animal):
    def __init__(self, type_, food, category):
        super().__init__(type_)
        self.food = food
        self.category = category

    def show(self):
        print("Pet Animal Details:")
        print(f"Type     : {self.type}")
        print(f"Food     : {self.food}")
        print(f"Category : {self.category}")
        print("-" * 30)


# Create one object of each child class
wild_animal = WildAnimal("Lion", "Roar", "Golden")
pet_animal = PetAnimal("Dog", "Meat & Kibble", "Domestic")

# Use show() method to display the records of both animals
wild_animal.show()
pet_animal.show()

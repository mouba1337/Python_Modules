"""
This module demonstrates inheritance by creating specialized plant types.
"""


class Plant:
    """
    A base class representing a generic plant.
    """
    def __init__(self, name, height, age):
        """
        Initializes a new Plant.
        """
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    A specialized plant type for flowers.
    """
    def __init__(self, name, height, age, color):
        """
        A specialized plant type for Flowers.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """
        Prints the blooming action.
        """
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """
    A specialized plant type for trees.
    """
    def __init__(self, name, height, age, trunk_diameter):
        """
        Initializes a Tree, inhereting from plant.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        Calculates and prints the shade area.
        """
        shade = (self.height * self.trunk_diameter) // 320
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    """
    A specialized plant type for vegetables.
    """
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """
        Initializes a Vegetable, inheriting from plant.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


print("=== Garden Plant Types ===\n")

rose = Flower("Rose", 25, 30, "red")

print(f"{rose.name} (Flower): {rose.height}cm, "
      f"{rose.age} days,{rose.color} color")

rose.bloom()

print()

oak = Tree("Oak", 500, 1825, 50)

print(f"{oak.name} (Tree): {oak.height}cm, {oak.age} days, "
      f"{oak.trunk_diameter}cm diameter")

oak.produce_shade()

print()

tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")

print(f"{tomato.name} (Vegetable): {tomato.height}cm, {tomato.age} days, "
      f"{tomato.harvest_season} harvest")
print(f"{tomato.name} is rich in {tomato.nutritional_value}")

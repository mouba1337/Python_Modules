"""
This module simulates plant growth through instance methods.
"""


class Plant:
    """
    A class representing a plant with name, height, and age.
    """
    def __init__(self, name, height, age):
        """
        It runs automatically when we create a new Plant().
        """
        self.name = name
        self.height = height
        self.age = age

    def grow(self, size):
        """
        Increases the plant's height by the given size.
        """
        self.height += size

    def age_plant(self, days):
        """
        Increases the plant's age by the given days.
        """
        self.age += days

    def get_info(self):
        """
        Returns the plant status.
        """
        return f"{self.name}: {self.height}cm, {self.age} days old"


print("=== Day 1 ===")

plant1 = Plant("Rose", 25, 30)

print(plant1.get_info())

plant1.grow(6)
plant1.age_plant(6)

print("=== Day 7 ===")
print(plant1.get_info())
print("Growth this week: +6cm")

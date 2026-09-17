"""
This module demonstrates a factory-style creation of multiple Plant objects.
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


rose = Plant("Rose", 25, 30)
oak = Plant("Oak", 200, 365)
cactus = Plant("Cactus", 5, 90)
sunflower = Plant("Sunflower", 80, 45)
fern = Plant("Fern", 15, 120)

print("Plant Factory Output =")
print(f"Created: {rose.name} ({rose.height}cm, {rose.age} days)")
print(f"Created: {oak.name} ({oak.height}cm, {oak.age} days)")
print(f"Created: {cactus.name} ({cactus.height}cm, {cactus.age} days)")
print(f"Created: {sunflower.name} "
      f"({sunflower.height}cm, {sunflower.age} days)")
print(f"Created: {fern.name} ({fern.height}cm, {fern.age} days)")
print("\nTotal plants created: 5")

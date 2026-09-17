"""
This module implements data encapsulation to protect plant information.
"""


class SecurePlant:
    """
    A secure plant class that protects data from corruption through validation.
    """
    def __init__(self, name, height, age):
        """
        Initializes a new Plant.
        """
        self.name = name
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height):
        """
        Setter: Validates that height is a positive number.
        """
        if height < 0:
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age):
        """
        Setter: Validates that age is a positive number.
        """
        if age < 0:
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self):
        """
        Getter: Returns the plant's height.
        """
        return self._height

    def get_age(self):
        """
        Getter: Returns the plant's age.
        """
        return self._age


print("=== Garden Security System ===")
print("Plant created: Rose")

rose = SecurePlant("Rose", 25, 30)
print()
print("Invalid operation attempted: height -5cm [REJECTED]")

rose.set_height(-5)

print()
print(f"Current plant: {rose.name} ({rose.get_height()}cm, "
      f"{rose.get_age()} days)")

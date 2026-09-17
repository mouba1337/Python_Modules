
class GardenError(Exception):
    """
    class for garden problems
    """
    pass


class PlantError(GardenError):
    """
    For problems with plants
    """
    pass


class WaterError(GardenError):
    """
    For problems with water
    """
    pass


def test_custom_error():
    """
    Demonstrates raising and catching custom exceptions.
    """
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        raise PlantError("the tomato plant is wilting!\n")
    except PlantError as e:
        print(f"Caught Planterror: {e}")
    try:
        print("Testing WaterError...")
        raise WaterError("Not enough water in the tank!\n")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")


if __name__ == "__main__":
    test_custom_error()
    print("All custom error types work correctly!")

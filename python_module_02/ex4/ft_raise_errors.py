
def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Validates plant health metrics.
    Returns a success message if valid.
    """
    if not plant_name:
        raise ValueError("Plant name cannot be empty!\n")
    if not (1 <= water_level <= 10):
        if water_level > 10:
            raise ValueError(f"Water level {water_level}"
                             "is too high (max 10)\n")
        else:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
    if not (2 <= sunlight_hours <= 12):
        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours}"
                             " is too low (min 2)\n")
    return f"Plant '{plant_name}' is healthy!\n"


def test_plant_checks():
    """
    Tests check_plant_health with various valid
    and invalid inputs to verify error raising.
    """
    print("=== Garden Plant Health Checker ===\n")
    tests = [
        ("tomato", 5, 8, "Testing good values..."),
        ("", 5, 8, "Testing empty plant name..."),
        ("lettuce", 15, 8, "Testing bad water level..."),
        ("rose", 5, 0, "Testing bad sunlight hours...")
    ]
    for name, water, sun, message in tests:
        print(message)
        try:
            msg = check_plant_health(name, water, sun)
            print(msg)
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    test_plant_checks()
    print("All error raising tests completed!")

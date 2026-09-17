
def water_plants(plant_list):
    """
    Iterates through a list of plants to simulate watering.
    """
    try:
        print("Opening watering system")
        for plant in plant_list:
            print(f"Watering {plant + ''}")
    except: # noqa
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """
     Tests water_plants with both a valid list and a list containing None.
    """
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")
    print("\nTesting with errors...")
    water_plants(["tomato", None, "carrots"])


if __name__ == "__main__":
    test_watering_system()
    print("\nCleanup always happens, even with errors!")


class GardenError(Exception):
    """Base exception for garden management."""
    pass


class PlantError(GardenError):
    """Exception for plant-related errors."""
    pass


class WaterError(GardenError):
    """Exception for watering-related errors."""
    pass


class GardenManager:
    """
    Manages garden operations including adding plants,
    watering, and health checks.
    """
    def __init__(self):
        """Initialize the garden with an empty plant list."""
        self.plants = []

    def add_plant(self, plant_name):
        """
        Adds a plant to the list. Raises PlantError if the name is empty.
        """
        try:
            if not plant_name:
                raise PlantError("Plant name cannot be empty!")
            self.plants.append(plant_name)
            print(f"Added {plant_name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        """
        Simulates watering all plants in the list.
        """
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        except Exception as e:
            print(f"Error watering: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water, sun):
        """
        Checks health metrics for a specific plant.
        """
        if water > 10:
            print(f"Error checking {plant_name}: "
                  f"Water level {water} is too high (max 10)")
        else:
            print(f"{plant_name}: healthy (water: {water}, sun: {sun})")


if __name__ == "__main__":
    print("=== Garden Management system ===\n")
    manager = GardenManager()
    print("Adding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    manager.add_plant("")
    print("\nWatering plants...")
    manager.water_plants()
    print("\nChecking plant health...")
    manager.check_plant_health("tomato", 5, 8)
    manager.check_plant_health("lettuce", 15, 8)
    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and coninuing...")
    print("\nGarden management system test complete!")

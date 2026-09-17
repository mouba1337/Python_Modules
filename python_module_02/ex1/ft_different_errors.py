
def garden_operations():
    """
    Demonstrates specific exception handling for different scenarios.
    """
    print("=== Garden Error Types Demo ===\n")
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")
    try:
        print("Testing ZeroDivisionError...")
        print(10 / 0)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")
    try:
        print("Testing FileNotFoundError...")
        open("missing.txt", "r")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")
    try:
        print("Testing KeyError...")
        dic = {"ginger": "yellow"}
        print(dic["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")
    print("Testing multiple errors together...")
    try:
        print(10 / 0)
    except (ValueError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    garden_operations()


def check_temperature(temp_str):
    """
    Validates temperature input.
    Returns the temperature if valid, otherwise handles errors prints message.
    """
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            return temp
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input():
    """
    Demonstrates the pipeline with various inputs as per subject requirements.
    """
    print("=== Garden Temperature Checker ===\n")
    lst = ["25", "abc", "100", "-50"]
    for t in lst:
        print(f"Testing temperature: {t}")
        result = check_temperature(t)
        if result is not None:
            print(f"Temperature {result}°C is perfect for plants!")
        print()


if __name__ == "__main__":
    test_temperature_input()
    print("All tests completed - program didn't crash!")

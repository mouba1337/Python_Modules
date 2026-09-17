def ft_garden_summary():
    """
    Asks for a garden name and the number of plants, then displays a summary.
    """
    name = input("Enter garden name: ")
    number = int(input("Enter number of plants: "))
    print(f"Garden: {name}")
    print(f"Plants: {number}")
    print("Status: Growing well!")

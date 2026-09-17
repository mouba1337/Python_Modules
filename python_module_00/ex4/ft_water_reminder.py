def ft_water_reminder():
    """
    asks for the number of days since last watering.
    """
    watering = int(input("Days since last watering: "))
    if watering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")

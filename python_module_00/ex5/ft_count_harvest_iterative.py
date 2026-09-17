def ft_count_harvest_iterative():
    """
    Counts up the days until harvest using a loop.
    """
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")

def ft_count_harvest_recursive(day=1, lastday=None):
    """
    counts days to harvest using recursion
    """
    if lastday is None:
        lastday = int(input("Days until harvest: "))
    if day > lastday:
        print("Harvest time!")
        return
    print(f"Day {day}")
    ft_count_harvest_recursive(day + 1, lastday)

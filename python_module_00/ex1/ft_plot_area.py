def ft_plot_area():
    """
    Calculates and displays the area of a garden plot based on user input.
    """
    lengthin = input("Enter length: ")
    widthin = input("Enter width: ")
    length = int(lengthin)
    width = int(widthin)
    area = length * width
    print(f"Plot area: {area}")

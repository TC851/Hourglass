print("Sandglasses in digital versions:")


def printSandglass(width: int):
    if width < 3:
        print("Width must be greater than 2")
        return
    height = (width + 1) // 2
    for i in range(height):
        num_spaces = abs(height - i - 1)
        num_stars = width - (2 * num_spaces)
        output = ' ' * num_spaces + '*' * num_stars + ' ' * num_spaces
        print(output)


# main--------------------------------------------
printSandglass(7)
printSandglass(9)
printSandglass(2)


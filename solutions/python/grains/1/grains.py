def square(number):
    """
        Calculates the number of grains on given square.

        :param number: int - The number of square
    """
    
    if 64 >= number >= 1:
        return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    total = 0 

    for i in range(0,64):
        total += 2 ** i

    return total

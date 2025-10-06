def is_armstrong_number(number):
    """
        Checks if the given number is 'armstrong number'

        :param number: int - the number which should check
        :return boolean
    """    

    length_of_number = len(str(number))
    total = 0


    for i in range(0,length_of_number):
        total += int(str(number)[i]) ** length_of_number
    
    return total == number

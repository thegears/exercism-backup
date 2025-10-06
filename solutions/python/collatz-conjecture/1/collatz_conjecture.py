def steps(number):
    """
        Gives number of steps which given number reachs 1

        :param number: int - the number which will reach 1
        :return int - number of steps 
    """

    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    process_number = number
    number_of_steps = 0

    while process_number != 1:
        if process_number % 2 == 0:
            process_number /= 2
        else:
            process_number = (process_number * 3) + 1
        number_of_steps += 1


    return number_of_steps
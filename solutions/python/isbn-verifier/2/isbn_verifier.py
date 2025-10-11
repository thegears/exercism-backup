def is_valid(isbn:str):

    """
        Takes a ISBN for checking and returns its ISBN or not

        :param ISBN: str - ISBN to check
        :return boolean - is it ISBN or not
    """

    total = 0
    alphabets = "abcdefghijklmnopqrstuvwyz"

    isbn = isbn.translate(str.maketrans("","","-"))
    isbn_list = list(isbn)

    if len(isbn_list) != 10: return False
    if any(e.lower() in alphabets for e in isbn_list): return False
    if "X" in isbn_list and isbn_list[-1] != "X": return False

    

    for i in range(1,11):
        char = isbn_list[i-1]
        total += int("10" if char == "X" else char) * (11 - i)


    return total % 11 == 0

def leap_year(year):
    """
        Checks the given year is leap

        :param year: int - the year to be checked
        :return boolean - gives is year leap or not
    """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
def checkIsTriangle(sides):

    """
        Checks whether the given triangle is correct

        :param sides: int - triangle
        :return boolean: correct or incorrect
    """

    a,b,c = sides

    return abs(a-b) < c < a+b and abs(a-c) < b < a+c and abs(b-c) < a < b+c

def equilateral(sides):
    return checkIsTriangle(sides) and sides.count(sides[0]) == 3


def isosceles(sides):
    checkIsTriangle(sides)
    return checkIsTriangle(sides) and any(sides.count(e) > 1 for e in sides)


def scalene(sides):
    checkIsTriangle(sides)
    return checkIsTriangle(sides) and all(sides.count(e) == 1 for e in sides)

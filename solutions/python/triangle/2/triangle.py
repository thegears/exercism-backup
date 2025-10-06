def valid_triangle(f):
    def inner(sides):
        a,b,c = sides
        return abs(a-b) < c < a+b and abs(a-c) < b < a+c and abs(b-c) < a < b+c and f(sides)
    return inner

@valid_triangle
def equilateral(sides):
    return sides.count(sides[0]) == 3

@valid_triangle
def isosceles(sides):
    return any(sides.count(e) > 1 for e in sides)

@valid_triangle
def scalene(sides):
    return all(sides.count(e) == 1 for e in sides)

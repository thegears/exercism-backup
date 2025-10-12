def score(x, y):
    locate = x**2 + y**2
    if locate > 100:
        return 0
    elif locate > 25:
        return 1
    elif locate > 1:
        return 5
    else:
        return 10

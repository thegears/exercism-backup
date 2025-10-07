def is_isogram(string):
    string = string.lower()
    string =  ''.join(x for x in string if x.isalpha())
    for l in string:
        if string.count(l) > 1: return False
    return True

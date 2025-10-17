color_codes = [
    {"name": "black", "code": 0},
    {"name": "brown", "code": 1},
    {"name": "red", "code": 2},
    {"name": "orange", "code": 3},
    {"name": "yellow", "code": 4},
    {"name": "green", "code": 5},
    {"name": "blue", "code": 6},
    {"name": "violet", "code": 7},
    {"name": "grey", "code": 8},
    {"name": "white", "code": 9},
]


def color_code(color):
    return next(i for i in color_codes if i["name"] == color)["code"]


def colors():
    return list(map(lambda x: x["name"], color_codes))

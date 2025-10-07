def convert(number:int):
    text = ""
    if not number % 3: text += "Pling"
    if not number % 5: text+="Plang"
    if not number % 7: text += "Plong"

    return str(number) if text == "" else text 

def response(hey_bob:str):
    hey_bob = hey_bob.translate(str.maketrans("","","\n\r\t "))
    return "Calm down, I know what I'm doing!" if hey_bob[-1:] == "?" and hey_bob.isupper() else  "Sure." if hey_bob[-1:] == "?" else "Whoa, chill out!" if hey_bob.isupper() else "Fine. Be that way!" if hey_bob == "" else "Whatever."
    

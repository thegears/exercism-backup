def rotate(text: str, key: int):
    text_list = list(text)
    new_text = ""
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    for l in text_list:
        if l.lower() not in alphabet: new_text += l
        else: 
            new_letter = alphabet[ (alphabet.index(l.lower()) + key) % 26 ]
            new_text +=  new_letter if not l.isupper() else new_letter.upper()

    return new_text


def is_pangram(sentence):
    english_alphabet = list(map(chr, range(97, 123)))

    for l in list(sentence.lower()):
        english_alphabet = list(filter(lambda e: e != l,english_alphabet))

    return len(english_alphabet) == 0

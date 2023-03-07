def get_count(sentence):
    c = 0
    vowels = ["a", "e", "i", "o", "u"]
    for s in sentence:
        if s in vowels:
            c += 1
    return c
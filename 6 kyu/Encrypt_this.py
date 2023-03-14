def encrypt_this(text):
    new_str = ""
    if len(text) > 1:
        for t in text.split(" "):
            new_str += str(ord(t[0]))
            if len(t) > 2:
                new_str += t[-1]
                new_str += t[2:-1]
                new_str += t[1]
            elif len(t) == 2:
                new_str += t[-1]
            new_str += " "
    return new_str[0:-1]
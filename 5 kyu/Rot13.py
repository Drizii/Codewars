def rot13(message):
    new_mess = ""
    for m in message:
        if m.isalpha():
            if m.islower():
                if ord(m)+13 > 122:
                    new_mess += chr(96 + (ord(m)+13 - 122))
                else:
                    new_mess += chr(ord(m)+13)
            else:
                if ord(m) + 13 > 90:
                    new_mess += chr(64 + (ord(m) + 13 - 90))
                else:
                    new_mess += chr(ord(m) + 13)
        else:
            new_mess += m
    return new_mess
def sum_digits(number):
    x = 0
    for i in str(abs(number)):
        x += int(i)
    return x
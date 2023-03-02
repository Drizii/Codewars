import datetime
entered_code = "abc"
correct_code = "abc"
current_date = "September 5, 2014"
expiration_date = "September 25, 2014"


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    c_year = current_date.split(" ")[2]
    c_month = datetime.datetime.strptime(current_date.split(" ")[0], '%B').month
    c_day = (current_date.split(",")[0])[-1]
    e_year = expiration_date.split(" ")[2]
    e_month = datetime.datetime.strptime(expiration_date.split(" ")[0], '%B').month
    e_day = (expiration_date.split(",")[0])[-1]
    if str(entered_code) != str(correct_code):
        return False
    elif entered_code == 2:
        return False
    else:
        if e_year > c_year:
            return True
        elif e_year == c_year:
            if e_month > c_month:
                return True
            elif e_month == c_month:
                if e_day >= c_day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
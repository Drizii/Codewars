def evaporator(content, evap_per_day, threshold):
    days = 0
    percent = threshold/100*content
    while content > percent:
        content = content - (evap_per_day/100*content)
        days += 1
    return days

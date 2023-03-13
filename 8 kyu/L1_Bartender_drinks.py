def get_drink_by_profession(param):
    my_dict = {
        "jabroni": "Patron Tequila",
        "school counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine",
        "politician": "Your tax dollars",
        "rapper": "Cristal",
    }
    for key, value in my_dict.items():
        if key == param.lower():
            return value
    return "Beer"
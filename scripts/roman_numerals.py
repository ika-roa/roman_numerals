def to_roman(number):
    result = ""

    if number == 5:
        result += "V"
    elif number == 4:
        result += "IV"
    else:
        for i in range(number):
            result += "I"
    return result

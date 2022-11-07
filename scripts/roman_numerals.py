def to_roman(number):
    result = ""
    if number == 4:
        result += "IV"
    else:
        for i in range(number):
            result += "I"
    return result

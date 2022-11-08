def to_roman(number):
    result = ""
    remaining = number

    if remaining >= 5:
        result += "V"
        remaining -= 5
    if remaining == 4:
        result += "IV"
    else:
        for i in range(remaining):
            result += "I"
    return result

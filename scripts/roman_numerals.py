def to_roman(number):
    result = ""
    remaining = number

    if remaining >= 9:
        result = append_digit(result, "IX")
        remaining -= 9

    if remaining >= 5:
        result = append_digit(result, "V")
        remaining -= 5

    if remaining >= 4:
        result = append_digit(result, "IV")
        remaining -= 4

    for i in range(remaining):
        result = append_digit(result, "I")

    return result


def append_digit(result, roman_digit):
    result += roman_digit
    return result


if __name__ == "__main__":
    print(to_roman(9))

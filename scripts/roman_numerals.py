def to_roman(number):
    result = ""
    remaining = number

    if remaining >= 9:
        result = append_digit(result, "IX")
        remaining = reduce_number_by_found_digit(remaining, 9)

    if remaining >= 5:
        result = append_digit(result, "V")
        remaining = reduce_number_by_found_digit(remaining, 5)

    if remaining >= 4:
        result = append_digit(result, "IV")
        remaining = reduce_number_by_found_digit(remaining, 4)

    for i in range(remaining):
        result = append_digit(result, "I")

    return result


def append_digit(result, roman_digit):
    result += roman_digit
    return result


def reduce_number_by_found_digit(remaining, arabic_digit):
    remaining -= arabic_digit
    return remaining


if __name__ == "__main__":
    print(to_roman(9))

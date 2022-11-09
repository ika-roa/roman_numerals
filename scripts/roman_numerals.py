ROMAN_DIGITS = ((1000, 'M'),
                (900, 'CM'),
                (500, 'D'),
                (400, 'CD'),
                (100, 'C'),
                (90, 'XC'),
                (50, "L"),
                (40, "XL"),
                (10, "X"),
                (9, "IX"),
                (5, "V"),
                (4, "IV"),
                (1, "I"))


def to_roman(number):
    result = ""
    remaining = number

    for arabic_digit, roman_digit in ROMAN_DIGITS:
        while remaining >= arabic_digit:
            result = append_digit(result, roman_digit)
            remaining = reduce_number_by_found_digit(remaining, arabic_digit)

    return result


def append_digit(result, roman_digit):
    result += roman_digit
    return result


def reduce_number_by_found_digit(remaining, arabic_digit):
    remaining -= arabic_digit
    return remaining


if __name__ == "__main__":
    print(to_roman(9))

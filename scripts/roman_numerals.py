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


class RomanNumeral:
    def to_roman(self, number):
        if self.input_is_valid(number):
            result = ""
            remaining = number

            for arabic_digit, roman_digit in ROMAN_DIGITS:
                while remaining >= arabic_digit:
                    result = self.append_digit(result, roman_digit)
                    remaining = self.reduce_number_by_found_digit(remaining, arabic_digit)

        return result

    def input_is_valid(self, number):
        if not isinstance(number, int):
            raise TypeError("Only integer numbers can be converted to Roman numerals")
        elif number < 0:
            raise ValueError("Romans did not know negative numbers.")
        elif number == 0:
            raise ValueError("Romans did not know the number 0.")
        elif number > 3999:
            raise ValueError("This number is too big to convert.")
        else:
            return True

    def append_digit(self, result, roman_digit):
        result += roman_digit
        return result

    def reduce_number_by_found_digit(self, remaining, arabic_digit):
        remaining -= arabic_digit
        return remaining


if __name__ == "__main__":
    print(RomanNumeral().to_roman(number=2))

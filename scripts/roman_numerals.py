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

    def __init__(self, number):
        if isinstance(number, int):
            self.int_number = number
            self.roman_number = self.to_roman(number)
        elif isinstance(number, str):
            self.int_number = self.to_int(number)
            self.roman_number = number
        else:
            raise TypeError("Please enter a roman number or an integer.")

    def to_roman(self, number):
        result = ""
        if self.input_is_valid_int(number):
            remaining = number
            for arabic_digit, roman_digit in ROMAN_DIGITS:
                while remaining >= arabic_digit:
                    result = self.append_digit(result, roman_digit)
                    remaining = self.reduce_number_by_found_digit(remaining, arabic_digit)
        return result

    def to_int(self, roman_number):
        result = 0
        if self.input_is_valid_roman(roman_number):
            while len(roman_number) > 0:
                for arabic_digit, roman_digit in ROMAN_DIGITS:
                    if roman_number.startswith(roman_digit):
                        result += arabic_digit
                        roman_number = roman_number.replace(roman_digit, "", 1)
        return result

    def input_is_valid_int(self, number):
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

    def input_is_valid_roman(self, roman_number):
        if self.more_than_three_same_letters_in_a_row(roman_number):
            raise TypeError("This is not a Roman number, the same letter appears more than 3 times in a row.")
        elif self.wrong_letter_in(roman_number):
            raise TypeError("There is a wrong letter in the Roman number.")
        else:
            return True

    def more_than_three_same_letters_in_a_row(self, roman_number):
        last_char = ""
        counter = 0
        for char in roman_number:
            if char == last_char:
                counter += 1
                if counter > 2:
                    return True
            else:
                counter = 0
            last_char = char
        return False

    def wrong_letter_in(self, roman_number):
        roman_digits = [roman_digit for _, roman_digit in ROMAN_DIGITS]
        wrong_letters = [char for char in roman_number if char not in roman_digits]
        if wrong_letters:
            return True
        else:
            return False

    def append_digit(self, result, roman_digit):
        result += roman_digit
        return result

    def reduce_number_by_found_digit(self, remaining, arabic_digit):
        remaining -= arabic_digit
        return remaining


if __name__ == "__main__":
    print(RomanNumeral(9).roman_number)

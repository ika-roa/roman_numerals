import unittest

from scripts.roman_numerals import calculate_roman_numeral


class TestCalculateRomanNumeral(unittest.TestCase):

    def test_calculate_roman_num_for_1(self):
        result = "I"
        assert calculate_roman_numeral(1) == result

    def test_calculate_roman_num_for_2(self):
        result = "II"
        assert calculate_roman_numeral(2) == result

    def test_calculate_roman_num_for_3(self):
        result = "III"
        assert calculate_roman_numeral(3) == result

    def test_calculate_roman_num_for_4(self):
        result = "IV"
        assert calculate_roman_numeral(4) == result

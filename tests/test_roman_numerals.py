import unittest

from scripts.roman_numerals import calculate_roman_numeral


class TestCalculateRomanNumeral(unittest.TestCase):

    def test_calculate_roman_num_for_1(self):
        result = "I"
        assert calculate_roman_numeral(1) == result

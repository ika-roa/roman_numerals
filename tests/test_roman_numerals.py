import unittest

from scripts.roman_numerals import to_roman


class TestToRoman(unittest.TestCase):

    def test_to_roman_for_1(self):
        result = "I"
        assert to_roman(1) == result

    def test_to_roman_for_2(self):
        result = "II"
        assert to_roman(2) == result

    def test_to_roman_for_3(self):
        result = "III"
        assert to_roman(3) == result

    def test_to_roman_for_4(self):
        result = "IV"
        assert to_roman(4) == result

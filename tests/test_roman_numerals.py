import pytest
from scripts.roman_numerals import RomanNumeral

KNOWN_VALUES = ((1, 'I'),
                (2, 'II'),
                (3, 'III'),
                (4, 'IV'),
                (5, 'V'),
                (6, 'VI'),
                (7, 'VII'),
                (8, 'VIII'),
                (9, 'IX'),
                (10, 'X'),
                (50, 'L'),
                (100, 'C'),
                (500, 'D'),
                (1000, 'M'),
                (31, 'XXXI'),
                (148, 'CXLVIII'),
                (294, 'CCXCIV'),
                (312, 'CCCXII'),
                (421, 'CDXXI'),
                (528, 'DXXVIII'),
                (621, 'DCXXI'),
                (782, 'DCCLXXXII'),
                (870, 'DCCCLXX'),
                (941, 'CMXLI'),
                (1043, 'MXLIII'),
                (1110, 'MCX'),
                (1226, 'MCCXXVI'),
                (1301, 'MCCCI'),
                (1485, 'MCDLXXXV'),
                (1509, 'MDIX'),
                (1607, 'MDCVII'),
                (1754, 'MDCCLIV'),
                (1832, 'MDCCCXXXII'),
                (1993, 'MCMXCIII'),
                (2074, 'MMLXXIV'),
                (2152, 'MMCLII'),
                (2212, 'MMCCXII'),
                (2343, 'MMCCCXLIII'),
                (2499, 'MMCDXCIX'),
                (2574, 'MMDLXXIV'),
                (2646, 'MMDCXLVI'),
                (2723, 'MMDCCXXIII'),
                (2892, 'MMDCCCXCII'),
                (2975, 'MMCMLXXV'),
                (3051, 'MMMLI'),
                (3185, 'MMMCLXXXV'),
                (3250, 'MMMCCL'),
                (3313, 'MMMCCCXIII'),
                (3408, 'MMMCDVIII'),
                (3501, 'MMMDI'),
                (3610, 'MMMDCX'),
                (3743, 'MMMDCCXLIII'),
                (3844, 'MMMDCCCXLIV'),
                (3888, 'MMMDCCCLXXXVIII'),
                (3940, 'MMMCMXL'),
                (3999, 'MMMCMXCIX'),
                )


class TestToRoman:
    @pytest.mark.parametrize("test_input, expected", KNOWN_VALUES)
    def test_valid_numbers_are_converted_correctly(self, test_input, expected):
        assert RomanNumeral(test_input).roman_number == expected

    def test_0_as_input_throws_value_error(self):
        with pytest.raises(ValueError):
            RomanNumeral(0).roman_number

    def test_negative_number_as_input_throws_value_error(self):
        with pytest.raises(ValueError):
            RomanNumeral(-5).roman_number

    def test_too_big_number_as_input_throws_value_error(self):
        with pytest.raises(ValueError):
            RomanNumeral(5000).roman_number

    def test_invalid_input_throws_type_error(self):
        with pytest.raises(TypeError):
            RomanNumeral("A").to_roman("A")


class TestToInt:

    @pytest.mark.parametrize("expected, test_input", KNOWN_VALUES)
    def test_valid_numbers_are_converted_correctly(self, test_input, expected):
        assert RomanNumeral(test_input).int_number == expected

    def test_more_than_3_repeats_raises_type_error(self):
        with pytest.raises(TypeError):
            RomanNumeral("IIII").int_number

    def test_wrong_letter_raises_type_error(self):
        with pytest.raises(TypeError):
            RomanNumeral("IIB").int_number

import unittest
from scripts.fizzbuzz import calculate_fizzbuzz, FizzBuzz


class TestCalculateFizzBuzz(unittest.TestCase):

    def test_fizzbuzz_returns_bam_if_1_is_square(self):
        i = 1
        assert calculate_fizzbuzz(i) == "Bam"

    def test_fizzbuzz_returns_2_for_2(self):
        i = 2
        assert calculate_fizzbuzz(i) == i

    def test_fizzbuzz_returns_fizz_if_3_divisible_by_3(self):
        i = 3
        assert calculate_fizzbuzz(i) == "Fizz"

    def test_fizzbuzz_returns_bam_if_4_is_square(self):
        i = 4
        assert calculate_fizzbuzz(i) == "Bam"

    def test_fizzbuzz_returns_buzz_if_5_divisible_by_5(self):
        i = 5
        assert calculate_fizzbuzz(i) == "Buzz"

    def test_fizzbuzz_returns_woof_if_7_divisible_by_7(self):
        i = 7
        assert calculate_fizzbuzz(i) == "Woof"

    def test_fizzbuzz_returns_fizz_if_number_13_contains_3(self):
        i = 13
        assert calculate_fizzbuzz(i) == "Fizz"

    def test_fizzbuzz_returns_fizzbuzz_if_15_divisible_by_3_and_5(self):
        i = 15
        assert calculate_fizzbuzz(i) == "FizzBuzz"

    def test_fizzbuzz_returns_buzz_if_number_52_contains_5(self):
        i = 52
        assert calculate_fizzbuzz(i) == "Buzz"

    def test_fizzbuzz_returns_woof_if_number_71_contains_7(self):
        i = 71
        assert calculate_fizzbuzz(i) == "Woof"


class TestReturnFizzBuzzRange(unittest.TestCase):

    def test_fizzbuzz_range_1_to_100(self):
        fizz_100 = ['Bam', 2, 'Fizz', 'Bam', 'Buzz', 'Fizz', 'Woof', 8, 'FizzBam', 'Buzz',
                    11, 'Fizz', 'Fizz', 'Woof', 'FizzBuzz', 'Bam', 'Woof', 'Fizz', 19, 'Buzz',
                    'FizzWoof', 22, 'Fizz', 'Fizz', 'BuzzBam', 26, 'FizzWoof', 'Woof', 29, 'FizzBuzz',
                    'Fizz', 'Fizz', 'Fizz', 'Fizz', 'FizzBuzzWoof', 'FizzBam', 'FizzWoof', 'Fizz', 'Fizz',
                    'Buzz', 41, 'FizzWoof', 'Fizz', 44, 'FizzBuzz', 46, 'Woof', 'Fizz', 'WoofBam', 'Buzz',
                    'FizzBuzz', 'Buzz', 'FizzBuzz', 'FizzBuzz', 'Buzz', 'BuzzWoof', 'FizzBuzzWoof', 'Buzz', 'Buzz',
                    'FizzBuzz', 61, 62, 'FizzWoof', 'Bam', 'Buzz', 'Fizz', 'Woof', 68, 'Fizz', 'BuzzWoof',
                    'Woof', 'FizzWoof', 'FizzWoof', 'Woof', 'FizzBuzzWoof', 'Woof', 'Woof', 'FizzWoof', 'Woof', 'Buzz',
                    'FizzBam', 82, 'Fizz', 'FizzWoof', 'Buzz', 86, 'FizzWoof', 88, 89, 'FizzBuzz',
                    'Woof', 92, 'Fizz', 94, 'Buzz', 'Fizz', 'Woof', 'Woof', 'Fizz', 'BuzzBam']
        assert FizzBuzz(100).convert_range_to_fizzbuzz() == fizz_100

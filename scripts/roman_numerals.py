def calculate_fizzbuzz(i):
    output = ""

    if i % 3 == 0 or "3" in str(i):
        output += "Fizz"
    if i % 5 == 0 or "5" in str(i):
        output += "Buzz"
    if i % 7 == 0 or "7" in str(i):
        output += "Woof"
    if (i ** 0.5) % 1 == 0:
        output += "Bam"

    if output:
        return output
    else:
        return i


class FizzBuzz:

    def __init__(self, upper_limit):
        self.upper_limit = upper_limit

    def convert_range_to_fizzbuzz(self):
        return [calculate_fizzbuzz(i) for i in range(1, self.upper_limit + 1)]


if __name__ == "__main__":
    print(FizzBuzz(100).convert_range_to_fizzbuzz())

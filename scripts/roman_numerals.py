def to_roman(number):
    result = ""
    remaining = number

    if remaining >= 9:
        result += "IX"
        remaining -= 9

    if remaining >= 5:
        result += "V"
        remaining -= 5

    if remaining >= 4:
        result += "IV"
        remaining -= 4

    for i in range(remaining):
        result += "I"

    return result


if __name__ == "__main__":
    print(to_roman(9))

# symbol tables for both directions
VALUES = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
SYMBOLS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

# roman to integer: subtract when a smaller symbol precedes a bigger one
def roman_to_int(text):
    total = 0
    for i in range(len(text)):
        value = SYMBOLS[text[i]]
        if len(text) > i + 1 and SYMBOLS[text[i + 1]] > value:
            sign = -1
        else:
            sign = 1
        total = total + value * sign
    return total

# integer to roman using the greedy method
def int_to_roman(number):
    result = ""
    for value, symbol in VALUES:
        while value <= number:
            result = result + symbol
            number = number - value
    return result

def is_valid_roman(text):
    if not text:
        return False
    else:
        for ch in text:
            if ch not in SYMBOLS:
                return False
        return True

def main():
    count = int(input())
    converted = []
    for _ in range(count):
        item = input().strip().upper()
        if item.isdigit() and 3999 >= int(item) >= 1:
            converted.append(int_to_roman(int(item)))
        elif is_valid_roman(item):
            converted.append(str(roman_to_int(item)))
        else:
            converted.append("invalid")
    lengths = []
    for entry in converted:
        lengths.append(len(entry))
    longest = max(lengths, default=0)
    for i in range(len(converted)):
        print("{} {}".format(1 + i, converted[i]))
    print("longest answer %d" % longest)

main()

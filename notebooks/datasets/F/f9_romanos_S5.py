# symbol tables for both directions
VALUES = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
SYMBOLS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

# roman to integer: subtract when a smaller symbol precedes a bigger one
def roman_to_int(text):
    total = 0
    for i in range(len(text)):
        value = SYMBOLS[text[i]]
        sign = -1 if i + 1 < len(text) and value < SYMBOLS[text[i + 1]] else 1
        total += sign * value
    return total

# integer to roman using the greedy method
def int_to_roman(number):
    result = ""
    for value, symbol in VALUES:
        while number >= value:
            result += symbol
            number -= value
    return result

def is_valid_roman(text):
    if len(text) == 0:
        return False
    for ch in text:
        if not ch in SYMBOLS:
            return False
    return True

def main():
    count = int(input())
    converted = []
    for _ in range(0, count, 1):
        item = input().strip().upper()
        if item.isdigit() and 1 <= int(item) <= 3999:
            converted.append(int_to_roman(int(item)))
        else:
            if is_valid_roman(item):
                converted.append(str(roman_to_int(item)))
            else:
                converted.append("invalid")
    lengths = [len(entry) for entry in converted]
    longest = 0
    for size in lengths:
        if size > longest:
            longest = size
    for i in range(len(converted)):
        print(i + 1, converted[i])
    print("longest answer", longest)

main()

# symbol tables for both directions
NUMERALS = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
LETTERS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

# roman to integer: subtract when a smaller symbol precedes a bigger one
def to_int(numeral):
    acc = 0
    for pos in range(len(numeral)):
        val = LETTERS[numeral[pos]]
        if pos + 1 < len(numeral) and val < LETTERS[numeral[pos + 1]]:
            direction = -1
        else:
            direction = 1
        acc = acc + direction * val
    return acc

# integer to roman using the greedy method
def to_roman(num):
    out = ""
    for val, sym in NUMERALS:
        while num >= val:
            out = out + sym
            num = num - val
    return out

def valid(numeral):
    if len(numeral) == 0:
        return False
    for c in numeral:
        if not c in LETTERS:
            return False
    return True

def run():
    qty = int(input())
    answers = []
    for _ in range(qty):
        token = input().strip().upper()
        if token.isdigit() and 1 <= int(token) <= 3999:
            answers.append(to_roman(int(token)))
        elif valid(token):
            answers.append(str(to_int(token)))
        else:
            answers.append("invalid")
    sizes = []
    for ans in answers:
        sizes.append(len(ans))
    longest_len = max(sizes, default=0)
    for pos in range(len(answers)):
        print(pos + 1, answers[pos])
    print("longest answer", longest_len)

run()

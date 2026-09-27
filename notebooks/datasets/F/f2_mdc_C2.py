import math

# greatest common divisor with euclid's algorithm
def euclid(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# least common multiple of two numbers
def lcm_pair(x, y):
    return x // euclid(x, y) * y

# fold gcd and lcm over the whole list
def gcd_all(numbers):
    acc = numbers[0]
    for pos in range(1, len(numbers)):
        acc = euclid(acc, numbers[pos])
    return acc

def lcm_all(numbers):
    acc = 1
    for item in numbers:
        acc = lcm_pair(acc, item)
    return acc

def find_coprime(numbers):
    found = []
    for pos in range(len(numbers)):
        for other in range(pos + 1, len(numbers)):
            if euclid(numbers[pos], numbers[other]) == 1:
                found.append((numbers[pos], numbers[other]))
    return found

def run():
    data = []
    for word in input().split():
        num = abs(int(word))
        if num > 0 and num < 100000:
            data.append(num)
    if not data:
        print("no valid numbers")
        return
    gval = gcd_all(data)
    lval = lcm_all(data)
    if gval == math.gcd(*data):
        state = "ok"
    else:
        state = "mismatch"
    print("gcd", gval, "lcm", lval, state)
    found = find_coprime(data)
    acc_sum = 0
    for x, y in found:
        acc_sum = acc_sum + x + y
    print("coprime pairs:", len(found), "sum", acc_sum)

run()

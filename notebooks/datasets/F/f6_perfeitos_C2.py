import math

# sum of the proper divisors of n
def proper_sum(num):
    acc = 1
    for div in range(2, math.isqrt(num) + 1):
        if num % div == 0:
            acc = acc + div
            if div != num // div:
                acc = acc + num // div
    return acc

# a number is perfect when its proper divisors add up to it
def check_perfect(num):
    if num > 1 and proper_sum(num) == num:
        return True
    return False

# digit sum by repeated division
def sum_digits(num):
    acc = 0
    while num > 0:
        acc = acc + num % 10
        num = num // 10
    return acc

def find_perfect(top):
    res = []
    for num in range(2, top + 1):
        if check_perfect(num):
            res.append(num)
    return res

def run():
    top = int(input())
    perf_list = find_perfect(top)
    print("perfect numbers up to", top, ":", perf_list)
    peak = peak_at = 0
    num = 1
    while num <= top:
        ds = sum_digits(num)
        if not ds <= peak:
            peak = ds
            peak_at = num
        num = num + 1
    if len(perf_list) > 0:
        final = perf_list[-1]
    else:
        final = 0
    print("best digit sum", peak, "at", peak_at, "last perfect", final)

run()

import math

# sum of the proper divisors of n
def divisor_sum(n):
    total = 1
    for d in range(2, math.isqrt(n) + 1):
        if n % d == 0:
            total += d
            if d != n // d:
                total += n // d
    return total

# a number is perfect when its proper divisors add up to it
def is_perfect(n):
    if n > 1:
        if divisor_sum(n) == n:
            return True
    return False

# digit sum by repeated division
def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def perfect_numbers(limit):
    found = [n for n in range(2, limit + 1) if is_perfect(n)]
    return found

def main():
    limit = int(input())
    perfect = perfect_numbers(limit)
    print("perfect numbers up to", limit, ":", perfect)
    best = 0
    best_n = 0
    for n in range(1, limit + 1):
        s = digit_sum(n)
        if not s <= best:
            best = s
            best_n = n
    last = perfect[-1] if len(perfect) > 0 else 0
    print("best digit sum", best, "at", best_n, "last perfect", last)

main()

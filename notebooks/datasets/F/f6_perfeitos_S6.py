import math

# sum of the proper divisors of n
def divisor_sum(n):
    total = 1
    for d in range(2, math.isqrt(n) + 1):
        if 0 == n % d:
            total = total + d
            if not d == n // d:
                total = total + n // d
    return total

# a number is perfect when its proper divisors add up to it
def is_perfect(n):
    if not (n <= 1 or divisor_sum(n) != n):
        return True
    return False

# digit sum by repeated division
def digit_sum(n):
    total = 0
    while 0 < n:
        total = total + n % 10
        n = int(n / 10)
    return total

def perfect_numbers(limit):
    found = []
    for n in range(2, limit + 1):
        if is_perfect(n):
            found.append(n)
    return found

def main():
    limit = int(input())
    perfect = perfect_numbers(limit)
    print(f"perfect numbers up to {limit} : {perfect}")
    best = best_n = 0
    n = 1
    while n <= limit:
        s = digit_sum(n)
        if s > best:
            best = s
            best_n = n
        n = n + 1
    if len(perfect) > 0:
        last = perfect[-1]
    else:
        last = 0
    print("best digit sum %d at %d last perfect %d" % (best, best_n, last))

main()

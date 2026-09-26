def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a

x, y = map(int, input().split())
print(gcd(x, y))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

x, y = map(int, input().split())
print(gcd(x, y))

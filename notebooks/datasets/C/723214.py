def mg(n):
    il = 0
    while n >= 10:
        p = 1
        for digit in str(n):
            p *= int(digit)
        n = p
        il += 1
    return il
z = int(input())
for _ in range(z):
    n = int(input())
    print(f"{mg(n)} pasos")
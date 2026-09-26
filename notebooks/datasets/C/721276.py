def multiply_digits(n):
    cont = 0
    while n >= 10:
        prod = 1
        for digit in str(n):
            prod *= int(digit)
        n = prod
        cont += 1
    return cont

num_cases = int(input())
for _ in range(num_cases):
    n = int(input().strip())
    steps = multiply_digits(n)
    print(f"{steps} pasos")
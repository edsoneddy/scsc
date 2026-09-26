def digit_product(n):
    steps = 0
    while n >= 10:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        steps += 1
    return steps

num_cases = int(input())
for _ in range(num_cases):
    n = int(input())
    print(f"{digit_product(n)} pasos")
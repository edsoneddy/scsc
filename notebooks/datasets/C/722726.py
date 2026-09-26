def multiply_digits(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product

def count_steps_to_single_digit(n):
    if n == 0:
        return 0 
    steps = 0
    while n >= 10:
        n = multiply_digits(n)
        steps += 1
    return steps


num_cases = int(input())
for _ in range(num_cases):
    n = int(input())
    steps = count_steps_to_single_digit(n)
    print(f"{steps} pasos")


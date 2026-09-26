def multiply_digits(n):
    iterations = 0
    while n >= 10:
        digits = [int(d) for d in str(n)]
        n = 1
        for d in digits:
            n *= d
        iterations += 1
    return iterations

# Read the number of test cases
num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):
    n = int(input())
    iterations = multiply_digits(n)
    print(f"{iterations} pasos")
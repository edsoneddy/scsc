def digit_product(n):
    steps = 0
    while n >= 10:
        product = 1
        while n > 0:
            digit = n % 10
            product *= digit
            n //= 10
        n = product
        steps += 1
    return steps

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    test_cases = int(data[0])
    results = []

    for i in range(1, test_cases + 1):
        n = int(data[i])
        steps = digit_product(n)
        results.append(f"{steps} pasos")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()

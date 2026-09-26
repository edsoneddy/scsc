num_cases = int(input())

for _ in range(num_cases):
    size = int(input())
    vector_a = list(map(int, input().split()))
    vector_b = list(map(int, input().split()))
    scalar_product = sum(a * b for a, b in zip(vector_a, vector_b))
    print(scalar_product)

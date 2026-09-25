def dot_product(vector_a, vector_b):
    return sum(a * b for a, b in zip(vector_a, vector_b))
num_cases = int(input())
for _ in range(num_cases):
    size = int(input())  
    vector_a = list(map(int, input().split()))
    vector_b = list(map(int, input().split()))
    
    print(dot_product(vector_a, vector_b))


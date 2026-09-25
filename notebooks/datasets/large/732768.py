def dot_product(vector_a, vector_b):
    return sum(a * b for a, b in zip(vector_a, vector_b))

def main():
    import sys
    input_data = sys.stdin.read().strip().splitlines()
    
    index = 0
    test_cases = int(input_data[index])
    index += 1
    results = []
    
    for _ in range(test_cases):
        n = int(input_data[index])
        index += 1
        vector_a = list(map(int, input_data[index].strip().split()))
        index += 1
        vector_b = list(map(int, input_data[index].strip().split()))
        index += 1
        
        # Calcular el producto escalar
        result = dot_product(vector_a, vector_b)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
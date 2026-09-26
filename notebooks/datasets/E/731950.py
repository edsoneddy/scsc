def dot_product(A, B):
    return sum(a*b for a, b in zip(A, B))

def main():
    test_cases = int(input())
    results = []
    
    for _ in range(test_cases):
        n = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        result = dot_product(A, B)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

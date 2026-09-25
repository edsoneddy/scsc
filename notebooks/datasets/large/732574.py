def producto_escalar(a, b):
    
    return sum(x * y for x, y in zip(a, b))

try:
    t = int(input())  
    
    for _ in range(t):
    
        n = int(input())
        
        A = list(map(int, input().split()))

        B = list(map(int, input().split()))
        
        print(producto_escalar(A, B))

except Exception as e:
    print(f"Error: {e}")
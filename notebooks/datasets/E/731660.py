casos = int(input().strip())

for _ in range(casos):

    n = int(input().strip())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    producto = sum(a * b for a, b in zip(a, b))

    print(producto)

num_casos = int(input())
 
for _ in range(num_casos):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    producto_escalar = sum(x * y for x, y in zip(a, b))
    print(producto_escalar)
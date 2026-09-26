n = int(input())
for i in range(n):
    p = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    productos = []
    for j in range(p):
        productos.append(a[j] * b[j])
    print(sum(productos))
    
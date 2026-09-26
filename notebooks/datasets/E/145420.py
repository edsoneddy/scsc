casos = int(input())
for i in range(casos):
    longitud = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = []
    for j in range(longitud):
        res.append(a[j]*b[j])
    print(sum(res))
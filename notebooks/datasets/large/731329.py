#pEscalar
N = int(input())
for i in range(N):
    elem = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    Pes = []
    for j in range(elem):
        Pes.append(a[j] * b[j])
    print(sum(Pes))
casos = int(input())
for i in range(casos):
    n = int(input())
    vecA = list(map(int, input().split()))
    vecB = list(map(int, input().split()))
    prod = sum(a * b for a, b in zip(vecA, vecB))
    print(prod)
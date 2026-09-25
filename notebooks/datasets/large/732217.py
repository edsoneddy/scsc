def escalar():
    count = 0
    for i in range(n):
        count += A[i] * B[i]
    print(count)

for _ in range(int(input())):
    n = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    escalar()
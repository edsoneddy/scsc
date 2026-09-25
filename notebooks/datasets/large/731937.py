from sys import stdin
for l in stdin:
    n = int(l)
    for _ in range(n):
        t = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        p= sum(A[i] * B[i] for i in range(t))
        print(p)
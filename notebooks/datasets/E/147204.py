n = int(input())
for x in range(n):
    tv = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s = 0
    for i in range(tv):
        s = s + (a[i]*b[i])
    print(s)
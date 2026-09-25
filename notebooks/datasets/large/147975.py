n=int(input())
for i in range(n):
    s = 0
    m = int(input())
    x = [0] * m
    x = input().split()
    y = [0] * m
    y = input().split()
    for j in range(m):
        s = s + int(x[j]) * int(y[j])
    print(s)

n=int(input())
for i in range(n):
    s = 0
    nn = int(input())
    x = [0] * nn
    x = input().split()
    y = [0] * nn
    y = input().split()
    for j in range(nn):
        s = s + int(x[j]) * int(y[j])
    print(s)
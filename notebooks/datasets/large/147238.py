n=input()
for w in range(int(n)):
    s = 0
    r = input()
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(len(a)):
        s=s+a[i]*b[i]
    print(s)

n=int(input())
for i in range(n):
    ca=int(input())
    x1=input().split()
    x2=input().split()
    v1=[]
    v2=[]
    c=0
    for j in x1:
        da = int(j)
        v1.insert(c, da)
        c = c + 1
    c=0
    for j in x2:
        da = int(j)
        v2.insert(c, da)
        c = c + 1
    s=0
    c=0
    for i in range(ca):
        s=s+(v1[c]*v2[c])
        c=c+1
    print(s)
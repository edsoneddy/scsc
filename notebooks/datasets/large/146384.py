h=int(input())
for i in range (h):
    c=int(input())
    a=input().split()
    b=input().split()
    d=-1
    e=[]
    while d<c-1:
        d=d+1
        e.append((int(a[d])*int(b[d])))
    f=0
    for g in e:
        f=f+g
    print(f)
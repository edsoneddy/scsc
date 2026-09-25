def prodesc(a,b):
    c=0
    for i in range(len(a)):
        c+=a[i]*b[i]
    return c

x=int(input())
L=[]
for _ in range(x):
    y = int(input())
    a=map(int,input().split())
    b=map(int,input().split())
    L.append(prodesc(list(a),list(b)))
print(*L,sep="\n")
def prod(n):
    c=1
    for k in str(n):
        c=c*int(k)
    return c

def iter(n):
    c=0
    while len(str(n))>1:
        c=c+1
        n=prod(n)
    return c

L=[]
x=int(input())
for i in range(x):
    y=int(input())
    L=L+[f'{iter(y)} pasos']
print(*L,sep="\n")
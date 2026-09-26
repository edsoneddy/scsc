a=int(input())
g=0
x=0
y=0
suma=0
for i in range(a):
    s=int(input())
    b=s+1
    d = input().split()
    f = input().split()
    for o in range(s):
        x=int(d[g])
        y=int(f[g])
        suma=suma + ( x * y )
        g+=1
    print(suma)
    g=0
    suma=0


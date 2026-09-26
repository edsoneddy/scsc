m=int(input())
for j in range(m):
    n=int(input())
    v=[]
    v2=[]
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    suma=0
    for i in range(n):
        suma=suma+x[i]*y[i]
    print(suma)
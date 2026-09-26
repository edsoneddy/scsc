for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    suma=0;
    for j in range(n):
        suma+=a[j]*b[j]
    print(suma)
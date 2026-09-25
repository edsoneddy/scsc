def multiplicador(a, b):
    return a*b
 
n= int(input())
for i in range(n):
    x = int(input())
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    suma= 0
    for j in range(x):
        suma += multiplicador(v1[j], v2[j])
    print(suma)
    
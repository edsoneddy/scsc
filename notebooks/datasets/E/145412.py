casos=int(input())
for i in range(casos):
    elementos=int(input())
    arrayA=list(map(int,input().split()))
    arrayB = list(map(int, input().split()))
    suma=0
    for a in range(elementos):
        suma=suma+(arrayA[a]*arrayB[a])
    print(suma)
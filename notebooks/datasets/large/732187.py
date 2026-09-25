
casos=int(input())
for i in range(casos):
    tamaño=int(input())
    vectorA=list(map(int,input().split()))
    vectorB=list(map(int,input().split()))
    resultado=0
    for i in range(tamaño):
        producto=vectorA[i]*vectorB[i]
        resultado+=producto
    print(resultado)        
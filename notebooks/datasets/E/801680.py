n=int(input())
for i in range(n):
    sumatoria=0
    n=int(input())
    lista=list(map(int, input().split()))
    lista2=list(map(int, input().split()))
    for i in range(len(lista)):
        sumatoria+=(lista[i]*lista2[i])
    print(sumatoria)
n=int(input())
resultados=[]
for i in range(n):
    entrada=int(input())
    cadena1=list(map(int, input().split()))
    cadena2=list(map(int, input().split()))
    prooducto=0
    for j in range(0,len(cadena1)):
        prooducto+=cadena1[j]*cadena2[j]

    resultados.append(prooducto)

for imprimir in resultados:
    print(imprimir)

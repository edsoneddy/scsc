def sumaDig(n):
    numero=1
    while(n>0):
        numero*=n%10
        n=n//10
    return numero
for i in range(int(input())):
    numero=int(input())
    cont=0
    while(numero>9):
        numero=sumaDig(numero)
        cont+=1
    print(cont, "pasos")
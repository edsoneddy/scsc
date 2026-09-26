n=int(input())
for i in range(n):
    a=input()
    aux=""
    cd=0
    for j in range(len(a)):
        if(a[j]==" "):
            aux=aux+" "
        else:
            if(cd%2==0):
                aux=aux+a[j].upper()
            else:
                aux=aux+a[j].lower()
            cd=cd+1
    print(aux)

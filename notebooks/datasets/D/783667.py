n=int(input())
for i in range(n):
    cad=input()
    aux=""
    c=0
    for j in cad:
        if j==" ":
            aux=aux+j
        else:
            if c%2==0:
                aux=aux+j.upper()
            else:
                aux=aux+j.lower()
            c=c+1
    print(aux)
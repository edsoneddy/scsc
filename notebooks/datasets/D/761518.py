for _ in range(int(input())):
    n=input()
    cont=0
    c=""
    for i in range(len(n)):
        if n[i]==" ":
            c=c+" "
        else:
            if cont==0:
                c=c+n[i].upper()
                cont=1
            else:
                c=c+n[i].lower()
                cont=0
    print(c)
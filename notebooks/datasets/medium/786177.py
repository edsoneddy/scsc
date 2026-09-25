def convertir(x):
    s=''
    a=True
    for i in x:
        if i.isalpha():
            if a:
                s=s+i.upper()
            else:
                s=s+i.lower()
            a = not a
        else:
            s=s+i
    return s

m=int(input())
for i in range(m):
    x=str(input())
    print(convertir(x))
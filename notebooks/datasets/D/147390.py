m=int(input())
c=''
for i in range(m):
    n=input()
    f=1
    for letra in n:
        if letra==' ':
            c+=letra
        else:
            if f%2==0:
                letra=letra.lower()
                f=f+1
                c+=letra
            else:
                letra=letra.upper()
                f=f+1
                c+=letra
    print(c)
    c=''
def please(g,r,cad):
    tam=len(cad)
    for j in range (tam):
        a=ord(cad[j])
        if 65<=a<=90:
            if g==1:
               r=r+(cad[j].upper())
               g=2
            elif g==2:
                r=r+(cad[j].lower())
                g=1
        else:
            end=(" ")
            r=r+end
    return r
n=int(input())
g=1
for i in range (n):
    r=str()
    cad=input()
    cad=cad.upper()
    r=please(g,r,cad)
    print(r)

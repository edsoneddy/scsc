
#c=c.upper()
def bailarin(cad):
    x=list(cad)
    z=len(x)
    sw=0
    for i in range(z):
        if x[i]!=" ":
            if sw == 0:
                x[i] = x[i].upper()
                sw = 1
            else:
                x[i] = x[i].lower()
                sw = 0
            print(x[i], end='')
        else:
            print(end=' ')
    print()

n=int(input())
for i in range(n):
    cad=str(input())
    bailarin(cad)

casos=int(input())
for i in range(casos):
    cadena=input()
    cadena=list(cadena)
    c=0
    new=[]
    for j in cadena:
        if c%2==0 and j!=" ":
            x=j.upper()
            new.append(x)
            c=c+1
        elif c%2==1 and j!=" ":
            x=j.lower()
            new.append(x)
            c=c+1
        if j==" ":
            new.append(" ")
    print("".join(new))
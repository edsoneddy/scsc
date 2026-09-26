def baila(x):
    s=1
    new=""
    for i in range(len(x)):
        if x[i]!=" ":
            if s%2==1:
                new=new+x[i].upper()
            else:
                new=new+x[i].lower()
            s=(s+1)%2
        else:
            new=new+" "
    return(new)
t=int(input())
for i in range(t):
    x=input()
    print(baila(x))
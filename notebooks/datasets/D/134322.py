n=int(input())
for t in range(n):
    cad=input()
    c=0
    for i in cad:
        if c%2==0 and i!=" ":
            print(i.upper(),end="")
            c=c+1
        elif i==" ":

            print(end=" ")
        else:
            print(i.lower(),end="")
            c=c+1
    print()
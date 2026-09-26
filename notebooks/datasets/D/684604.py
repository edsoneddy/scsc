n=int(input())
for i in range(1,n+1,1):
    v=input()
    sw=0
    for j in range(len(v)):
        if v[j]==" ":
            print(" ", end="")
            continue
        elif sw==0:
            print(v[j].upper(), end="")
            sw=1
        else:
            print(v[j].lower(), end="")
            sw=0
    print()
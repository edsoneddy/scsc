p=int(input())
for j in range(p):
    cad=input()
    n=len(cad)
    s= ""
    sw=0
    for i in range(0,n,1):
        if (cad[i]!=" "): 
            x=ord(cad[i])
            if (x>=97 and x<=122 and sw==0):
                sw=1
                x=x-32
                x=chr(x)
                s=s+x
            elif (x>=65 and x<=90 and sw==0):
                sw=1
                x=chr(x)
                s=s+x
            elif (x>=65 and x<=90 and sw==1):
                sw=0
                x=x+32
                x=chr(x)
                s=s+x
            else:
                sw=0
                x=chr(x)
                s=s+x
        else:
            s=s+" "
    print(s)
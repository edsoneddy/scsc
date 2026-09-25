def bailarina(x):
    nue=""
    c=0
    for a in range(len(x)):
        if c%2==0 and x[a]!=" ":
            nue=nue+x[a].upper()
        if c%2==1 and x[a]!=" ":
            nue=nue+x[a].lower()
        c=c+1
        if x[a]==" ":
            nue=nue+" "
            c=c-1
    return nue

N=int(input())
for i in range (N):
    x=input()
    print (bailarina(x))
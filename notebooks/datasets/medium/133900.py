n=int(input())
for i in range (1,n+1,1):
    s=str(input())
    r=len(s)
    res=""
    d=2
    for x in range(r):
        m=s[x]
        if m==" ":
            res=res+" "
        else:
            if d%2==0:
                t=m.upper()
                res=res+t
                d=d+1
            else:
                t =m.lower()
                res = res + t
                d = d + 1
    print(res)

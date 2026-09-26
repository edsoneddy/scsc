def dividirdigitos(n):
    l=[]
    while n>0:
        t=n%10
        l.append(t)
        n//=10
    return l

c=int(input())
for _ in range(c):
    n=int(input())
    v=0
    while n>9:
        l=dividirdigitos(n)
        m=1
        for i in l:
            m=m*i
            n=m
        v+=1
    print(v,'pasos') 

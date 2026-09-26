def per(n,pasos) :
    if(len(str(n))==1) :
        print(pasos,'pasos')
        return
    digitos= [int(i) for i in str(n)]
    res=1
    pasos+=1
    for j in digitos:
        res*=j
    per(res,pasos)
for x in range(int(input())):
    n=int(input())
    per(n,0)

def numero_a_vector(n):
    return list(map(int, str(n)))

t=int(input())
for _ in range(t):
    n=int(input())
    v=numero_a_vector(n)
    p=0
    s=1
    if(len(v)==1):
        print(p,"pasos")
    else:
        while(len(v)!=1):
            s=1
            p=p+1
            for i in range(len(v)):
                s *= v[i]
            v=numero_a_vector(s)
        print(p,"pasos")
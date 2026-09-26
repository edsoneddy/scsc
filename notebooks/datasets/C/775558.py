import math
def producto(w, c=0):
    a=list(str(w))
    s=list(map(int, a))
    s1=math.prod(s)
    if len(s)==1:
        return c
    else:
        c+=1
        return(producto(s1,c))

n=int(input())
a = []
for i in range(n):
    m=int(input())
    a.append(str(producto(m))+" "+"pasos")
print("\n".join(a))
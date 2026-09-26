def ed(n):
    return str(n).isdigit() and len(str(n)) == 1
def md(n):
    p=1
    for d in str(n):
        p*=int(d)
    return p
n=int(input())
for _ in range(1,n+1):
    c=0
    x=int(input())
    while not ed(x):
        x=md(x)
        c+=1
    print(c,"pasos")
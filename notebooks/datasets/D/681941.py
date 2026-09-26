T=int(input())
for _ in range(T):
    c=input()
    r=""
    m=True
    for l in c:
        if l.isalpha():
            r+=l.upper() if m else l.lower()
            m=not m
        else:
            r+=l
    print(r)            
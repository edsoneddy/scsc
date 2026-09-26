x = int(input())
for _ in range(x):
    cad = input()
    res = ""
    m= True
    for c in cad:
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
            if m:
                res += c.upper()
            else:
                res += c.lower()
            m = not m
        else:
            res += c
    print(res)
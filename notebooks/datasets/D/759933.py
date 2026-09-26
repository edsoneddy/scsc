def conv_bailarina(cad):
    res = ""
    alt_mayus = True
    for c in cad:
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
            if alt_mayus:
                res += c.upper()
            else:
                res += c.lower()
            alt_mayus = not alt_mayus
        else:
            res += c
    return res

n = int(input())
cads = [input() for _ in range(n)]

for cad in cads:
    print(conv_bailarina(cad))

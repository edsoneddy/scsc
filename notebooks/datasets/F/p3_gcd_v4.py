def mcd(u, v):
    while u != v:
        if u > v:
            u = u - v
        else:
            v = v - u
    return u


linea = input()
vals = [int(t) for t in linea.split()]
if vals[0] == 0:
    print(vals[1])
elif vals[1] == 0:
    print(vals[0])
else:
    print(mcd(vals[0], vals[1]))

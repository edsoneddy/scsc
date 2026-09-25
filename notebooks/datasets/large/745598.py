import sys
import re
def f1(a):
    b = a.split('\n')
    c = []
    d = ""    
    for e in b:
        e = e.strip()
        if e.endswith('-'):
            d += e[:-1]
        else:
            d += e
            c.extend(re.sub(r'[^\w-]', ' ', d).split())
            d = ""   
    f = set(g.lower() for g in c)
    h = sorted(f)    
    return h

i = sys.stdin.read()
j = f1(i)

for k in j:
    print(k)
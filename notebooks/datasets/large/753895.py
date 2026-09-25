#Milan Calixto Calle V 1.9
import sys
import re
d = set()
c = ""

for l in sys.stdin:
    l = l.rstrip()
    if l.endswith('-'):
        c += l[:-1]
    else:
        c += l
        p = re.findall(r'[a-zA-Z-]+', c)
        for w in p:
            d.add(w.lower())
        c = ""

for w in sorted(d):
    print(w)

def pasos_hasta_un_digito(s):
    if len(s) == 1:
        return 0

    pasos = 0
    while len(s) > 1:
        pasos += 1
        producto = 1
        for c in s:
            producto *= int(c)
        s = str(producto)
    return pasos

import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n_str = sys.stdin.readline().strip()
    pasos = pasos_hasta_un_digito(n_str)
    print(f"{pasos} pasos")
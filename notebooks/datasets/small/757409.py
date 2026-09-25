from sys import stdin

pila = []
res = []
for linea in stdin:
    op = linea.strip()
    if op[0] == 'S':
        _, x = op.split()
        pila.append(int(x))
    elif op[0] == 'A':
        if pila:
            res.append(str(max(pila)))
        else:
            res.append("Error")
    elif op[0] == 'R':
        if pila:
            pila.remove(max(pila))
        else:
            res.append("Error")
    elif op[0] == 'I':
        _, x = op.split()
        if pila:
            pila[pila.index(max(pila))] += int(x)
        else:
            res.append("Error")
    elif op[0] == 'D':
        _, x = op.split()
        if pila:
            pila[pila.index(max(pila))] -= int(x)
        else:
            res.append("Error")
    elif op[0] == 'T':
        break

for r in res:
    print(r)
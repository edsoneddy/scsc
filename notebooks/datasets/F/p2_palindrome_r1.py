def es_capicua(texto):
    limpio = []
    for c in texto:
        if c.isalnum():
            limpio.append(c.lower())
    izq = 0
    der = len(limpio) - 1
    while izq < der:
        if limpio[izq] != limpio[der]:
            return False
        izq += 1
        der -= 1
    return True

linea = input()
if es_capicua(linea):
    print("yes")
else:
    print("no")

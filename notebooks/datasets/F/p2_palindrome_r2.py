def es_capicua(texto):
    limpio = []
    for c in texto:
        if c.isalnum():
            limpio.append(c.lower())
    der = len(limpio) - 1
    izq = 0
    while izq < der:
        if limpio[izq] != limpio[der]:
            return False
        der -= 1
        izq += 1
    return True

linea = input()
if not es_capicua(linea):
    print("no")
else:
    print("yes")

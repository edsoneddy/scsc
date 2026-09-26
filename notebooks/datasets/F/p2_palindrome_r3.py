def es_capicua(texto):
    limpio = []
    for c in texto:
        if c.isalnum():
            limpio.append(c.lower())
    der = len(limpio) - 1
    n = len(limpio)
    for izq in range(n // 2):
        if limpio[izq] != limpio[der]:
            return False
        der -= 1
    return True

linea = input()
if not es_capicua(linea):
    print("no")
else:
    print("yes")

def es_capicua(texto):
    limpio = []
    for c in texto:
        if c.isalnum():
            limpio.append(c.lower())
    return limpio == limpio[::-1]

linea = input()
if not es_capicua(linea):
    print("no")
else:
    print("yes")

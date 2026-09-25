t = int(input())
for _ in range(t):
    linea = input()
    resultado = ""
    usar_mayus = True
    for c in linea:
        if c.isalpha():
            resultado += c.upper() if usar_mayus else c.lower()
            usar_mayus = not usar_mayus
        else:
            resultado += c
    print(resultado)

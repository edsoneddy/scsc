L = int(input())

for _ in range(L):
    cad = input().upper()
    resultado = ""
    sw = True
    for c in cad:
        if c == ' ':
            resultado += c
        else:
            resultado += c if sw else c.lower()
            sw = not sw
    print(resultado)

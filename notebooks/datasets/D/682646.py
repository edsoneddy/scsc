def bailarina(cad):
    res = ""
    mayus = True
    for char in cad:
        if char.isalpha():
            if mayus:
                res += char.upper()
            else:
                res += char.lower()
            mayus = not mayus
        else:
            res += char
    return res

T = int(input())
for _ in range(T):
    cadena = input()
    resultado = bailarina(cadena)
    print(resultado)

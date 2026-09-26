t=int(input())
for i in range(t):
    cad = input()
    c, cadena = 1, ""
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in cad:
        if i.upper() in abc:
            if c % 2 == 1:
                cadena = cadena + i.upper()
                c += 1
            else:
                cadena = cadena + i.lower()
                c += 1
        else:
            cadena = cadena + i
    print(cadena)
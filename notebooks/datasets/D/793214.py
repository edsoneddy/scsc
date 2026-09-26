T = int(input());

for _ in range (T):
    palabra = str(input());
    cadena = [];
    mayus = True;

    for p in palabra:
        if p == " ":
            cadena.append(p);
        else:
            if mayus:
                if 'a' <= p <= 'z':
                    p = chr(ord(p)-32);
            else:
                if 'A' <= p <= 'Z':
                    p = chr(ord(p) + 32);
            cadena.append(p)
            mayus = not mayus
    print("".join(cadena))
def bailarina(palabra):
    r = []
    mayus = True
    for letra in palabra:
        if letra.isalpha():
            if mayus:
                r.append(letra.upper())
            else:
                r.append(letra.lower())
            mayus = not mayus
        else:
            r.append(letra)
    return "".join(r)
t = int(input())
for _ in range(t):
    palabra = input()
    print(bailarina(palabra))
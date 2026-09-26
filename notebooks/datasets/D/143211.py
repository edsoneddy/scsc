casos = int(input())
for j in range(casos):
    palabra = input()
    c = 0
    for i in range(len(palabra)):
        letra = palabra[i]
        if letra == " ":
            c = c - 1
        elif c % 2 == 0:
            letra = letra.upper()
        else:
            letra = letra.lower()
        print(letra, end="")
        c = c + 1
    print()
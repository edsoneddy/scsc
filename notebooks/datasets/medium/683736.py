n = int(input())
for _ in range(n):
    frase = input()
    sw = False
    for char in frase:
        if char != ' ':  # Si el caracter no es un espacio
            if sw:
                print(char.lower(), end="")
                sw = False
            else:
                print(char.upper(), end="")
                sw = True
        else:  # Si el caracter es un espacio, no cambia el case
            print(char, end="")
    print()

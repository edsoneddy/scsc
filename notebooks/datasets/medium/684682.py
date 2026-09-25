x = int(input())
for _ in range(x):
    cadena = input()
    y = False
    for letra in cadena:
        if letra != ' ':  
            if y:
                print(letra.lower(), end="")
                y = False
            else:
                print(letra.upper(), end="")
                y = True
        else:
            print(letra, end="")
    print()
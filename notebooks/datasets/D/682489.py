n = int(input())
for _ in range(n):
    frase = input()
    sw = False
    for char in frase:
        if char != ' ':  
            if sw:
                print(char.lower(), end="")
                sw = False
            else:
                print(char.upper(), end="")
                sw = True
        else:
            print(char, end="")
    print()

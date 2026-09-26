#3.11
for _ in range(int(input())):
    n = input()
    resultado = ""
    flag_mayuscula = True
    for c in n:
        if c.isalpha():
            if flag_mayuscula:
                resultado += c.upper()
            else:
                resultado += c.lower()
            flag_mayuscula = not flag_mayuscula
        else:
            resultado += c
    print(resultado)
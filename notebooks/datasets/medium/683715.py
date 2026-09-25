T = int(input())
for _ in range(T):
    texto = input()
    bailarina = ""
    mayuscula = True
    for letra in texto:
        if letra.isalpha():
            if mayuscula:
                bailarina += letra.upper()
            else:
                bailarina += letra.lower()
            mayuscula = not mayuscula
        else:
            bailarina += letra
    print(bailarina)
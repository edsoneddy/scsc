n = int(input())
for _ in range(n):
    cadena = input()
    c = 0
    bailarina = ""
    for letra in cadena:
        if letra == " ":
            bailarina += letra
        else:
            if c % 2 == 0:
                bailarina += letra.upper()
            else:
                bailarina += letra.lower()
            c += 1
    print(bailarina)
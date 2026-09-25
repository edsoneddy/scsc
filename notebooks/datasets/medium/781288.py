
n = int(input())
for _ in range(n):
    cadena = input()
    bailarina = ''
    contador = 0
    for letra in cadena:
        if letra == ' ':
            bailarina += letra
        else:
            if contador%2 == 0:
                bailarina += letra.upper()
            else:
                bailarina += letra.lower()
            contador +=1
    print(bailarina)

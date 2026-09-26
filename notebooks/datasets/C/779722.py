def bisiesto(n):
    if 1800<=n and n<=9999:
        if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
            frase = "si"
        else:
            frase = "no"
    return frase
n = int(input())
verdad = bisiesto(n)
print(verdad)
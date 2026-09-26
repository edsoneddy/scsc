def pasos_para_multiplicar_digitos(n):
    pasos=0
    while n>=10:
        producto=1
        for digito in str(n):
            producto*=int(digito)
        n=producto
        pasos+=1
    return pasos
        

y=int(input())
for _ in range(y):
    n=int(input())
    print(f"{pasos_para_multiplicar_digitos(n)} pasos")
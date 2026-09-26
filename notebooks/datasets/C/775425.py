def multiplicar_digitos(n):
    producto = 1
    for d in str(n):
        producto *= int(d)
    return producto

n= int(input())

for i in range(n):
    numero = input().strip()

    if numero == "0":
        print("0 pasos")
        continue

    pasos = 0
    while len(numero) > 1:
        numero = str(multiplicar_digitos(numero))
        pasos += 1

    print(f"{pasos} pasos")

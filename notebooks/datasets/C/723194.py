def multiplicar_digitos(n):
    if n == 0:
        return 0  
    pasos = 0
    while n >= 10:  
        producto = 1
        while n > 0:
            digito = n % 10  
            producto *= digito  
            n //= 10  
        n = producto  
        pasos += 1  
    return pasos

num_casos = int(input())
resultados = []

for _ in range(num_casos):
    n = int(input())
    pasos = multiplicar_digitos(n)
    resultados.append(f"{pasos} pasos")

for resultado in resultados:
    print(resultado)
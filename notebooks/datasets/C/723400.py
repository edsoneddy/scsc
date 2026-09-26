def multiplicar_digitos(n):
    pasos = 0
    while n >= 10:
        producto = 1
        while n > 0:
            producto *= n % 10
            n //= 10
        n = producto  
        pasos += 1  
    return pasos

def main():
    num_casos = int(input().strip())
    for _ in range(num_casos):
        n = int(input().strip())
        pasos = multiplicar_digitos(n)
        print(f"{pasos} pasos")
if __name__ == "__main__":
    main()

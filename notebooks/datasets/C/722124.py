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
    casos = int(input())
    for _ in range(casos):
        n = int(input())
        if n == 0:
            print("0 pasos")
        else:
            print(f"{multiplicar_digitos(n)} pasos")

if __name__ == "__main__":
    main()
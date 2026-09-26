def pasos_multiplicacion(n):
    if n == 0:
        return 0
    pasos = 0
    while n >= 10:
        producto = 1
        for digito in str(n):
            producto *= int(digito)
        n = producto
        pasos += 1
    return pasos

def main():
    import sys
    input_lines = sys.stdin.read().split()
    T = int(input_lines[0])
    casos = input_lines[1:T+1]
    for num in casos:
        n = int(num)
        pasos = pasos_multiplicacion(n)
        print(f"{pasos} pasos")

if __name__ == "__main__":
    main()
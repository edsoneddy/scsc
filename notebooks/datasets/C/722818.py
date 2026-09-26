def mult(n):
    pasos = 0
    while n >= 10:
        producto = 1
        for digito in str(n):
            producto *= int(digito)
        n = producto
        pasos += 1
    return pasos

while True:
    try:
        nc = int(input())
        for _ in range(nc):
            n = int(input())
            pasos = mult(n)
            print(f"{pasos} pasos")
        break
    except EOFError:
        break 
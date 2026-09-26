def multiplicar_digitos(n_str):
    producto = 1
    for digito in n_str:
        producto *= int(digito)
    return str(producto)

def solve():
    num_casos = int(input())
    for _ in range(num_casos):
        n_str = input()
        if n_str == '0':
            print("0 pasos")
            continue

        pasos = 0
        while len(n_str) > 1:
            n_str = multiplicar_digitos(n_str)
            pasos += 1
        print(f"{pasos} pasos")

if __name__ == "__main__":
    solve()
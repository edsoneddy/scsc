# Calcula la raiz digital de un numero
def digital_root(n):
    while n >= 10:
        # sumar los digitos
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        n = total
    return n

x = int(input())
print(digital_root(x))  # imprime resultado

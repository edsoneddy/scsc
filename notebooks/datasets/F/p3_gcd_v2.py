def maximo_comun_divisor(numero1, numero2):
    if numero2 == 0:
        return numero1
    return maximo_comun_divisor(numero2, numero1 % numero2)

entrada = input().split()
n1 = int(entrada[0])
n2 = int(entrada[1])
resultado = maximo_comun_divisor(n1, n2)
print(resultado)

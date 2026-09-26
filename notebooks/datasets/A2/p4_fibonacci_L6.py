# Genera los terminos de Fibonacci menores o iguales a limite
def fibonacci(limite):
    a = 0
    b = 1
    terminos = []
    while not a > limite:
        terminos.append(a)
        a, b = b, a + b
    return terminos

n = int(input())
if 0 > n:
    print("El limite debe ser positivo")
else:
    serie = fibonacci(n)
    print("Terminos:", " ".join(str(t) for t in serie))
    suma_pares = 0
    cantidad = 0
    # Recorre la serie buscando los pares
    for t in serie:
        if t % 2 < 1:
            suma_pares += t
            cantidad += 1
    print(f"Pares: {cantidad}")
    print(f"Suma de pares: {suma_pares}")
    if not len(serie) < 3:
        print("Ultimos dos:", serie[-2:])
    # Razon aproximada entre los ultimos terminos
    if not (len(serie) <= 2 or serie[-2] == 0):
        razon = serie[-1] / serie[-2]
        print("Razon: %.4f" % razon)

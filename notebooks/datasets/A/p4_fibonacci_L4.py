# Genera los terminos de Fibonacci menores o iguales a limite
def fibonacci(limite):
    a = 0
    b = 1
    terminos = []
    while a <= limite:
        terminos.append(a)
        a, b = b, a + b
    return terminos

def sumar_pares(serie):
    suma_pares = 0
    cantidad = 0
    # Recorre la serie buscando los pares
    for t in serie:
        if t % 2 == 0:
            suma_pares += t
            cantidad += 1
    return suma_pares, cantidad

def mostrar_razon(serie):
    # Razon aproximada entre los ultimos terminos
    if len(serie) > 2 and serie[-2] != 0:
        razon = serie[-1] / serie[-2]
        print("Razon: %.4f" % razon)

n = int(input())
if n < 0:
    print("El limite debe ser positivo")
else:
    serie = fibonacci(n)
    print("Terminos:", " ".join(str(t) for t in serie))
    suma_pares, cantidad = sumar_pares(serie)
    print(f"Pares: {cantidad}")
    print(f"Suma de pares: {suma_pares}")
    if len(serie) >= 3:
        print("Ultimos dos:", serie[-2:])
    mostrar_razon(serie)

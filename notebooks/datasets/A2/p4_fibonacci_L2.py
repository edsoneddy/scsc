# Genera los terminos de Fibonacci menores o iguales a limite
def generar(tope):
    x = 0
    y = 1
    acum = []
    while x <= tope:
        acum.append(x)
        x, y = y, x + y
    return acum

maximo = int(input())
if maximo < 0:
    print("El limite debe ser positivo")
else:
    fibs = generar(maximo)
    print("Terminos:", " ".join(str(valor) for valor in fibs))
    total_par = 0
    cuantos = 0
    # Recorre la serie buscando los pares
    for valor in fibs:
        if valor % 2 == 0:
            total_par += valor
            cuantos += 1
    print(f"Pares: {cuantos}")
    print(f"Suma de pares: {total_par}")
    if len(fibs) >= 3:
        print("Ultimos dos:", fibs[-2:])
    # Razon aproximada entre los ultimos terminos
    if len(fibs) > 2 and fibs[-2] != 0:
        cociente = fibs[-1] / fibs[-2]
        print("Razon: %.4f" % cociente)

def producto_escalar(casos):
    resultados = []
    for caso in casos:
        n, A, B = caso
        producto = sum(a * b for a, b in zip(A, B))
        resultados.append(producto)
    return resultados

# Leer la entrada
T = int(input())
casos = []

for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    casos.append((n, A, B))

# Calcular el producto escalar para cada caso
resultados = producto_escalar(casos)

# Imprimir los resultados
for resultado in resultados:
    print(resultado)
def buscar(lista, objetivo, inicio, fin):
    if inicio > fin:
        return -1
    centro = (inicio + fin) // 2
    valor = lista[centro]
    if valor == objetivo:
        return centro
    if valor > objetivo:
        return buscar(lista, objetivo, inicio, centro - 1)
    return buscar(lista, objetivo, centro + 1, fin)

cantidad = int(input())
numeros = [int(x) for x in input().split()]
buscado = int(input())
resultado = buscar(numeros, buscado, 0, len(numeros) - 1)
print(resultado)

INICIO = 0

def contar_intercambios(arreglo, tam):
    intercambios = INICIO
    idx = 0
    while idx < tam - 1:
        for pos in range(idx + 1, tam):
            if (arreglo[idx] > arreglo[pos]):
                temp = arreglo[idx]
                arreglo[idx] = arreglo[pos]
                arreglo[pos] = temp
                intercambios += 1
        idx += 1
    return intercambios

casos = int(input())
for _ in range(casos):
    tam = int(input())
    arreglo = list(map(int, input().split()))
    print(contar_intercambios(arreglo, tam))

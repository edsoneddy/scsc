casos = int(input())
for idx in range(casos):
    tam = int(input())  # tamano del vector
    arreglo = list(map(int, input().split()))
    # burbuja: contar intercambios
    intercambios = 0
    for idx in range(tam - 1):
        for pos in range(idx + 1, tam):
            if (arreglo[idx] > arreglo[pos]):
                temp = arreglo[idx]
                arreglo[idx] = arreglo[pos]
                arreglo[pos] = temp
                intercambios += 1
    print(intercambios)

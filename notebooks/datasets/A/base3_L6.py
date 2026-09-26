def contar_inversiones(arreglo):
    if len(arreglo) <= 1:
        return arreglo, 0
    medio = len(arreglo) // 2
    izq, inv_izq = contar_inversiones(arreglo[:medio])
    der, inv_der = contar_inversiones(arreglo[medio:])
    fusion = []
    i = j = 0
    inversiones = inv_izq + inv_der
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            fusion.append(izq[i])
            i += 1
        else:
            fusion.append(der[j])
            j += 1
            inversiones += len(izq) - i
    fusion.extend(izq[i:])
    fusion.extend(der[j:])
    return fusion, inversiones

casos = int(input())
for _ in range(casos):
    tam = int(input())
    arreglo = list(map(int, input().split()))
    _, total = contar_inversiones(arreglo)
    print(total)

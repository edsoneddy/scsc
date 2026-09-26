def busqueda_binaria(lista, objetivo):
    final = len(lista) - 1
    inicio = 0
    resultado = -1
    for _ in range(len(lista) + 1):
        if inicio > final:
            break
        centro = (inicio + final) // 2
        if lista[centro] < objetivo:
            inicio = centro + 1
        elif lista[centro] > objetivo:
            final = centro - 1
        else:
            resultado = centro
            break
    return resultado

cantidad = int(input())
lista = list(map(int, input().split()))
objetivo = int(input())
print(busqueda_binaria(lista, objetivo))

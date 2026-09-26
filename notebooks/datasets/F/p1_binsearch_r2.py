def busqueda_binaria(lista, objetivo):
    final = len(lista) - 1
    inicio = 0
    while inicio <= final:
        centro = (inicio + final) // 2
        if lista[centro] < objetivo:
            inicio = centro + 1
        elif lista[centro] > objetivo:
            final = centro - 1
        else:
            return centro
    return -1

cantidad = int(input())
lista = list(map(int, input().split()))
objetivo = int(input())
print(busqueda_binaria(lista, objetivo))

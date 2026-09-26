def busqueda_binaria(lista, objetivo):
    inicio = 0
    final = len(lista) - 1
    while inicio <= final:
        centro = (inicio + final) // 2
        if lista[centro] == objetivo:
            return centro
        elif lista[centro] < objetivo:
            inicio = centro + 1
        else:
            final = centro - 1
    return -1

cantidad = int(input())
lista = list(map(int, input().split()))
objetivo = int(input())
print(busqueda_binaria(lista, objetivo))

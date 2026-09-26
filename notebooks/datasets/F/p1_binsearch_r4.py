import bisect

def busqueda_binaria(lista, objetivo):
    posicion = bisect.bisect_left(lista, objetivo)
    if posicion < len(lista) and lista[posicion] == objetivo:
        return posicion
    return -1

cantidad = int(input())
lista = list(map(int, input().split()))
objetivo = int(input())
print(busqueda_binaria(lista, objetivo))

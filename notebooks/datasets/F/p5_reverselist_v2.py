class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


def construir(valores):
    if not valores:
        return None
    cabeza = Nodo(valores[0])
    actual = cabeza
    for v in valores[1:]:
        actual.siguiente = Nodo(v)
        actual = actual.siguiente
    return cabeza


def invertir(nodo, anterior=None):
    if nodo is None:
        return anterior
    siguiente = nodo.siguiente
    nodo.siguiente = anterior
    return invertir(siguiente, nodo)


def imprimir(nodo):
    partes = []
    while nodo:
        partes.append(str(nodo.dato))
        nodo = nodo.siguiente
    return " ".join(partes)


numeros = list(map(int, input().split()))
lista = construir(numeros)
lista_invertida = invertir(lista)
print(imprimir(lista_invertida))

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

def construir_lista(valores):
    cabeza = None
    cola = None
    for v in valores:
        nodo = Nodo(v)
        if cabeza is None:
            cabeza = nodo
            cola = nodo
        else:
            cola.siguiente = nodo
            cola = nodo
    return cabeza

def invertir_lista(cabeza):
    anterior = None
    actual = cabeza
    while actual is not None:
        siguiente_nodo = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente_nodo
    return anterior

def a_lista(cabeza):
    salida = []
    while cabeza is not None:
        salida.append(str(cabeza.valor))
        cabeza = cabeza.siguiente
    return salida

numeros = list(map(int, input().split()))
cabeza = construir_lista(numeros)
cabeza_invertida = invertir_lista(cabeza)
print(' '.join(a_lista(cabeza_invertida)))

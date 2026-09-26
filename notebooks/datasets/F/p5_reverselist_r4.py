class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

def construir_lista(valores):
    cola = None
    cabeza = None
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
    valores = []
    while cabeza is not None:
        valores.append(cabeza.valor)
        cabeza = cabeza.siguiente
    valores.reverse()
    return construir_lista(valores)

def a_lista(cabeza):
    salida = []
    while cabeza is not None:
        salida.append(str(cabeza.valor))
        cabeza = cabeza.siguiente
    return salida

numeros = list(map(int, input().split()))
cabeza = construir_lista(numeros)
cabeza_invertida = invertir_lista(cabeza)
texto_salida = ' '.join(a_lista(cabeza_invertida))
print(texto_salida)

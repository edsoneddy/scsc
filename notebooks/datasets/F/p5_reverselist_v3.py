class Elemento:
    __slots__ = ("valor", "sig")

    def __init__(self, valor):
        self.valor = valor
        self.sig = None


class ListaEnlazada:
    def __init__(self):
        self.inicio = None

    def agregar(self, valor):
        e = Elemento(valor)
        if self.inicio is None:
            self.inicio = e
            return
        cursor = self.inicio
        while cursor.sig is not None:
            cursor = cursor.sig
        cursor.sig = e

    def voltear(self):
        pila = []
        cursor = self.inicio
        while cursor is not None:
            pila.append(cursor.valor)
            cursor = cursor.sig
        salida = []
        while pila:
            salida.append(pila.pop())
        return salida


entrada = input().split()
l = ListaEnlazada()
for tok in entrada:
    l.agregar(int(tok))

resultado = l.voltear()
print(" ".join(map(str, resultado)))

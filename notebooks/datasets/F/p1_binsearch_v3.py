import sys


class Buscador:
    def __init__(self, datos):
        self.d = datos

    def indice_de(self, x):
        a, b = 0, len(self.d) - 1
        pos = -1
        encontrado = False
        while a <= b and not encontrado:
            m = a + (b - a) // 2
            if self.d[m] == x:
                pos = m
                encontrado = True
            elif self.d[m] < x:
                a = m + 1
            else:
                b = m - 1
        return pos


datos_entrada = sys.stdin.read().split("\n")
n = int(datos_entrada[0])
vec = list(map(int, datos_entrada[1].split()))
x = int(datos_entrada[2])

b = Buscador(vec)
print(b.indice_de(x))

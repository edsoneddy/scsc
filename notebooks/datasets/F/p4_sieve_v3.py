class GeneradorPrimos:
    def __init__(self, tope):
        self.tope = tope
        self.marcados = set()

    def procesar(self):
        salida = []
        p = 2
        while p <= self.tope:
            if p not in self.marcados:
                salida.append(p)
                m = p * p
                while m <= self.tope:
                    self.marcados.add(m)
                    m += p
            p += 1
        return salida


g = GeneradorPrimos(int(input()))
res = g.procesar()
print(' '.join(str(x) for x in res))

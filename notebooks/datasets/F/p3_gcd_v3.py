class Euclides:
    def calcular(self, p, q):
        while q:
            resto = p % q
            p = q
            q = resto
        return p


datos = input()
partes = datos.split(" ")
a = int(partes[0])
b = int(partes[1])

e = Euclides()
print(e.calcular(a, b))

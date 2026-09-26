class Verificador:
    def __init__(self, texto):
        self.original = texto

    def _normalizar(self):
        resultado = []
        for ch in self.original:
            if ch.isalnum():
                resultado.append(ch.lower())
        return resultado

    def es_capicua(self):
        letras = self._normalizar()
        n = len(letras)
        for i in range(n // 2):
            if letras[i] != letras[n - 1 - i]:
                return False
        return True


v = Verificador(input())
print("yes" if v.es_capicua() else "no")

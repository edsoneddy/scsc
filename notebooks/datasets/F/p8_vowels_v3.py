class ContadorLetras:
    VOCALES = "aeiouAEIOU"

    def __init__(self, texto):
        self.texto = texto
        self.vocales = 0
        self.consonantes = 0

    def procesar(self):
        indice = 0
        while indice < len(self.texto):
            c = self.texto[indice]
            if c.isalpha():
                if c in self.VOCALES:
                    self.vocales += 1
                else:
                    self.consonantes += 1
            indice += 1


entrada = input()
cl = ContadorLetras(entrada)
cl.procesar()
print(cl.vocales, cl.consonantes)

class Combinador:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def resultado(self):
        junto = self.x + self.y
        junto.sort()
        return junto


entrada1 = list(map(int, input().split()))
entrada2 = list(map(int, input().split()))
c = Combinador(entrada1, entrada2)
salida = c.resultado()
print(" ".join(map(str, salida)))

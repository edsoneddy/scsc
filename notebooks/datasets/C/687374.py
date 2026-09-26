class Operaciones:
    def __init__(self): 
        self.numbers = []
    def guardar(self, x):
        self.numbers.append(x)
    def imprimir(self):
        print(max(self.numbers, default="Error"))
    def extraer(self):
        try:
            self.numbers.remove(max(self.numbers))
        except ValueError:
            print("Error")
    def incrementar(self, x):
        try:
            self.numbers[self.numbers.index(max(self.numbers))] += x
        except ValueError:
            print("Error")
    def decrementar(self, x):
        try:
            self.numbers[self.numbers.index(max(self.numbers))] -= x
        except ValueError:
            print("Error")
if __name__ == "__main__":
    ops = Operaciones()
    acciones = {
        "S": lambda x: ops.guardar(int(x)),
        "A": lambda _: ops.imprimir(),
        "R": lambda _: ops.extraer(),
        "I": lambda x: ops.incrementar(int(x)),
        "D": lambda x: ops.decrementar(int(x)),
    }
    while True:
        instruccion = input().split()
        if instruccion[0] == "T":
            break
        acciones.get(instruccion[0], lambda x: None)(instruccion[1] if len(instruccion) > 1 else None)
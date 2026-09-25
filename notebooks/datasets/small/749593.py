import heapq

class SistemaNumeros:
    def __init__(self):
        self.numeros = []
        
    def guardar(self, x):
        heapq.heappush(self.numeros, -x)
        
    def imprimir_maximo(self):
        if not self.numeros:
            print("Error")
            return
        print(-self.numeros[0])
        
    def extraer_maximo(self):
        if not self.numeros:
            print("Error")
            return
        return -heapq.heappop(self.numeros)
        
    def incrementar_maximo(self, x):
        if not self.numeros:
            print("Error")
            return
        maximo = -heapq.heappop(self.numeros)
        maximo += x
        heapq.heappush(self.numeros, -maximo)
        
    def decrementar_maximo(self, x):
        if not self.numeros:
            print("Error")
            return
        maximo = -heapq.heappop(self.numeros)
        maximo -= x
        heapq.heappush(self.numeros, -maximo)

def main():
    sistema = SistemaNumeros()
    
    while True:
        try:
            entrada = input().strip()
            if entrada == "T":
                break
                
            partes = entrada.split()
            operacion = partes[0]
            
            if operacion == "S":
                x = int(partes[1])
                sistema.guardar(x)
            elif operacion == "A":
                sistema.imprimir_maximo()
            elif operacion == "R":
                sistema.extraer_maximo()
            elif operacion == "I":
                x = int(partes[1])
                sistema.incrementar_maximo(x)
            elif operacion == "D":
                x = int(partes[1])
                sistema.decrementar_maximo(x)
                
        except EOFError:
            break

if __name__ == "__main__":
    main()

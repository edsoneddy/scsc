import heapq

class SistemaNumeros:
    def __init__(self):
        # Usamos un maxheap (multiplicamos por -1 para simular max heap con min heap)
        self.numeros = []
        
    def guardar(self, x):
        # S x : guarda una copia de un número x
        heapq.heappush(self.numeros, -x)  # Negativo para max heap
        
    def imprimir_maximo(self):
        # A : Imprime el número más grande
        if not self.numeros:
            print("Error")
            return
        print(-self.numeros[0])  # Negativo para obtener el valor original
        
    def extraer_maximo(self):
        # R : extrae el número más grande
        if not self.numeros:
            print("Error")
            return
        return -heapq.heappop(self.numeros)  # Negativo para obtener el valor original
        
    def incrementar_maximo(self, x):
        # I x : incrementa el número más grande en x
        if not self.numeros:
            print("Error")
            return
        maximo = -heapq.heappop(self.numeros)  # Extraer y convertir a positivo
        maximo += x  # Incrementar
        heapq.heappush(self.numeros, -maximo)  # Volver a insertar como negativo
        
    def decrementar_maximo(self, x):
        # D x : decrementa el número más grande en x
        if not self.numeros:
            print("Error")
            return
        maximo = -heapq.heappop(self.numeros)  # Extraer y convertir a positivo
        maximo -= x  # Decrementar
        heapq.heappush(self.numeros, -maximo)  # Volver a insertar como negativo

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
                # Guardar número
                x = int(partes[1])
                sistema.guardar(x)
            elif operacion == "A":
                # Imprimir máximo
                sistema.imprimir_maximo()
            elif operacion == "R":
                # Extraer máximo
                sistema.extraer_maximo()
            elif operacion == "I":
                # Incrementar máximo
                x = int(partes[1])
                sistema.incrementar_maximo(x)
            elif operacion == "D":
                # Decrementar máximo
                x = int(partes[1])
                sistema.decrementar_maximo(x)
                
        except EOFError:
            break

if __name__ == "__main__":
    main()

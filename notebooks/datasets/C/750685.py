import heapq

class AdministradorNumeros:
    def __init__(self):
        # Usamos un maxheap (simulado con min heap usando valores negativos)
        self.cola_prioridad = []
        
    def almacenar(self, valor):
        # S valor: guarda una copia de un número valor
        heapq.heappush(self.cola_prioridad, -valor)  # Negativo para max heap
        
    def mostrar_maximo(self):
        # A: Imprime el número más grande
        if not self.cola_prioridad:
            print("Error")
            return
        print(-self.cola_prioridad[0])  # Negativo para obtener el valor original
        
    def obtener_maximo(self):
        # R: extrae el número más grande
        if not self.cola_prioridad:
            print("Error")
            return
        return -heapq.heappop(self.cola_prioridad)  # Negativo para obtener el valor original
        
    def aumentar_maximo(self, incremento):
        # I incremento: incrementa el número más grande en incremento
        if not self.cola_prioridad:
            print("Error")
            return
        maximo = -heapq.heappop(self.cola_prioridad)  # Extraer y convertir a positivo
        maximo += incremento  # Incrementar
        heapq.heappush(self.cola_prioridad, -maximo)  # Volver a insertar como negativo
        
    def reducir_maximo(self, decremento):
        # D decremento: decrementa el número más grande en decremento
        if not self.cola_prioridad:
            print("Error")
            return
        maximo = -heapq.heappop(self.cola_prioridad)  # Extraer y convertir a positivo
        maximo -= decremento  # Decrementar
        heapq.heappush(self.cola_prioridad, -maximo)  # Volver a insertar como negativo

def ejecutar():
    gestor = AdministradorNumeros()
    
    while True:
        try:
            comando = input().strip()
            if comando == "T":
                break
                
            partes = comando.split()
            accion = partes[0]
            
            if accion == "S":
                # Almacenar número
                valor = int(partes[1])
                gestor.almacenar(valor)
            elif accion == "A":
                # Mostrar máximo
                gestor.mostrar_maximo()
            elif accion == "R":
                # Obtener máximo
                gestor.obtener_maximo()
            elif accion == "I":
                # Aumentar máximo
                incremento = int(partes[1])
                gestor.aumentar_maximo(incremento)
            elif accion == "D":
                # Reducir máximo
                decremento = int(partes[1])
                gestor.reducir_maximo(decremento)
                
        except EOFError:
            break

if __name__ == "__main__":
    ejecutar()

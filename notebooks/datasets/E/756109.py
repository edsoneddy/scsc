import sys
from collections import deque
import heapq

def adivinar_estructura(comandos):
    pila = []
    cola = deque()
    cola_prioridad = []
    
    es_pila = True
    es_cola = True
    es_cola_prioridad = True
    
    for tipo, x in comandos:
        if tipo == 1:  # Insertar elemento
            pila.append(x)
            cola.append(x)
            heapq.heappush(cola_prioridad, -x)  # Negativo para simular cola de prioridad (máximos)
        elif tipo == 2:  # Extraer elemento
            if es_pila:
                if not pila or pila.pop() != x:
                    es_pila = False
            if es_cola:
                if not cola or cola.popleft() != x:
                    es_cola = False
            if es_cola_prioridad:
                if not cola_prioridad or -heapq.heappop(cola_prioridad) != x:
                    es_cola_prioridad = False

    # Determinar la salida
    posibles = sum([es_pila, es_cola, es_cola_prioridad])
    if posibles == 0:
        return "impossible"
    elif posibles > 1:
        return "not sure"
    elif es_pila:
        return "stack"
    elif es_cola:
        return "queue"
    elif es_cola_prioridad:
        return "priority queue"

def main():
    input = sys.stdin.read
    datos = input().strip().splitlines()
    
    i = 0
    resultados = []
    
    while i < len(datos):
        n = int(datos[i].strip())
        i += 1
        
        comandos = []
        for _ in range(n):
            tipo, x = map(int, datos[i].strip().split())
            comandos.append((tipo, x))
            i += 1
        
        resultados.append(adivinar_estructura(comandos))
    
    # Imprimir resultados
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()

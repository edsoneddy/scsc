from collections import deque
import sys
import heapq

def determinar_estructura(n, operaciones):
    # Inicializar estructuras de datos
    pila = []
    cola = deque()
    cola_prioridad = []
    
    es_pila = True
    es_cola = True
    es_cola_prioridad = True
    
    for operacion in operaciones:
        tipo, x = operacion
        
        if tipo == 1:  # Operación de inserción
            pila.append(x)
            cola.append(x)
            heapq.heappush(cola_prioridad, -x)  # Negativo para simular max-heap
        
        elif tipo == 2:  # Operación de extracción
            if es_pila:
                if not pila or pila.pop() != x:
                    es_pila = False
            if es_cola:
                if not cola or cola.popleft() != x:
                    es_cola = False
            if es_cola_prioridad:
                if not cola_prioridad or -heapq.heappop(cola_prioridad) != x:
                    es_cola_prioridad = False

    # Determinar el resultado
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
    datos = input().strip().split("\n")
    
    i = 0
    resultados = []
    
    while i < len(datos):
        n = int(datos[i])
        i += 1
        operaciones = []
        
        for _ in range(n):
            tipo, x = map(int, datos[i].split())
            operaciones.append((tipo, x))
            i += 1
        
        resultado = determinar_estructura(n, operaciones)
        resultados.append(resultado)
    
    print("\n".join(resultados))

# Ejecutar el programa
if __name__ == "__main__":
    main()

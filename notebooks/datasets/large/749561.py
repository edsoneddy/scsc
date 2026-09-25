from collections import deque
import heapq
import sys
input = sys.stdin.read

def detectar_estructura(n, operaciones):
    # Inicializar las estructuras de datos
    pila = []
    cola = deque()
    cola_prioridad = []
    
    # Banderas para cada estructura
    es_pila = True
    es_cola = True
    es_cola_prioridad = True
    
    for tipo, x in operaciones:
        if tipo == 1:  # Insertar
            pila.append(x)
            cola.append(x)
            heapq.heappush(cola_prioridad, -x)  # Negativo para simular max-heap
        else:  # tipo == 2, extraer
            # Verificar pila
            if es_pila:
                if not pila or pila.pop() != x:
                    es_pila = False
                    
            # Verificar cola
            if es_cola:
                if not cola or cola.popleft() != x:
                    es_cola = False
                    
            # Verificar cola de prioridad
            if es_cola_prioridad:
                if not cola_prioridad or -heapq.heappop(cola_prioridad) != x:
                    es_cola_prioridad = False
    
    # Determinar resultado
    estructuras_posibles = []
    if es_pila:
        estructuras_posibles.append("stack")
    if es_cola:
        estructuras_posibles.append("queue")
    if es_cola_prioridad:
        estructuras_posibles.append("priority queue")
    
    # Retornar resultado según las estructuras posibles
    if len(estructuras_posibles) == 0:
        return "impossible"
    elif len(estructuras_posibles) == 1:
        return estructuras_posibles[0]
    else:
        return "not sure"

def main():
    data = input().strip().splitlines()
    i = 0
    results = []

    while i < len(data):
        n = int(data[i])
        i += 1
        operaciones = []

        for _ in range(n):
            tipo, x = map(int, data[i].split())
            operaciones.append((tipo, x))
            i += 1

        resultado = detectar_estructura(n, operaciones)
        results.append(resultado)

    print("\n".join(results))

if __name__ == "__main__":
    main()

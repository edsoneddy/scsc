from collections import deque
import heapq

def detectar_estructura():
    # Leer número de operaciones
    n = int(input())
    
    # Inicializar las estructuras de datos
    pila = []
    cola = deque()
    cola_prioridad = []
    
    # Banderas para cada estructura
    es_pila = True
    es_cola = True
    es_cola_prioridad = True
    
    # Guardar las operaciones
    operaciones = []
    for _ in range(n):
        tipo, x = map(int, input().split())
        operaciones.append((tipo, x))
        
        # Procesar operación
        if tipo == 1:  # Insertar
            pila.append(x)
            cola.append(x)
            heapq.heappush(cola_prioridad, -x)  # Negativo para simular max-heap
        else:  # tipo == 2, extraer
            # Verificar pila
            if es_pila:
                if len(pila) == 0 or pila.pop() != x:
                    es_pila = False
                    
            # Verificar cola
            if es_cola:
                if len(cola) == 0 or cola.popleft() != x:
                    es_cola = False
                    
            # Verificar cola de prioridad
            if es_cola_prioridad:
                if len(cola_prioridad) == 0 or -heapq.heappop(cola_prioridad) != x:
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
    # Procesar casos de prueba hasta EOF
    while True:
        try:
            resultado = detectar_estructura()
            print(resultado)
        except EOFError:
            break

if __name__ == "__main__":
    main()
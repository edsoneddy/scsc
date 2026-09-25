import heapq
from collections import deque

def detectar_estructura():
    n = int(input().strip())
    
    # Inicializar las estructuras de datos
    pila = []
    cola = deque()
    cola_prioridad = []
    
    # Bandera para las posibles estructuras
    es_pila = True
    es_cola = True
    es_cola_prioridad = True

    for _ in range(n):
        tipo, x = map(int, input().split())
        
        if tipo == 1:  # Comando de inserción
            if es_pila:
                pila.append(x)
            if es_cola:
                cola.append(x)
            if es_cola_prioridad:
                heapq.heappush(cola_prioridad, -x)  # Usar negativo para simular max heap
        elif tipo == 2:  # Comando de extracción
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

    # Determinar el resultado
    estructuras_posibles = []
    if es_pila:
        estructuras_posibles.append("stack")
    if es_cola:
        estructuras_posibles.append("queue")
    if es_cola_prioridad:
        estructuras_posibles.append("priority queue")

    # Determinar el mensaje final según las estructuras posibles
    if len(estructuras_posibles) == 1:
        return estructuras_posibles[0]
    elif len(estructuras_posibles) > 1:
        return "not sure"
    else:
        return "impossible"

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


from collections import deque
import heapq

def identificar_estructura():
    # Leer el número de operaciones
    cantidad_operaciones = int(input())
    
    # Inicializar las estructuras de datos
    pila_simulada = []
    cola_simulada = deque()
    prioridad_simulada = []
    
    # Banderas para cada estructura
    es_pila = True
    es_cola = True
    es_prioridad = True
    
    # Guardar las operaciones
    lista_operaciones = []
    for _ in range(cantidad_operaciones):
        accion, valor = map(int, input().split())
        lista_operaciones.append((accion, valor))
        
        # Procesar operación
        if accion == 1:  # Insertar
            pila_simulada.append(valor)
            cola_simulada.append(valor)
            heapq.heappush(prioridad_simulada, -valor)  # Negativo para simular max-heap
        else:  # accion == 2, extraer
            # Verificar pila
            if es_pila:
                if len(pila_simulada) == 0 or pila_simulada.pop() != valor:
                    es_pila = False
                    
            # Verificar cola
            if es_cola:
                if len(cola_simulada) == 0 or cola_simulada.popleft() != valor:
                    es_cola = False
                    
            # Verificar cola de prioridad
            if es_prioridad:
                if len(prioridad_simulada) == 0 or -heapq.heappop(prioridad_simulada) != valor:
                    es_prioridad = False
    
    # Determinar el resultado
    estructuras_posibles = []
    if es_pila:
        estructuras_posibles.append("stack")
    if es_cola:
        estructuras_posibles.append("queue")
    if es_prioridad:
        estructuras_posibles.append("priority queue")
    
    # Retornar el resultado según las estructuras posibles
    if len(estructuras_posibles) == 0:
        return "impossible"
    elif len(estructuras_posibles) == 1:
        return estructuras_posibles[0]
    else:
        return "not sure"

def ejecutar():
    # Procesar casos de prueba hasta EOF
    while True:
        try:
            resultado = identificar_estructura()
            print(resultado)
        except EOFError:
            break

if __name__ == "__main__":
    ejecutar()

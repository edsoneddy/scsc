import sys
import heapq

def determinar_estructura(comandos):
    pila = []
    cola = []
    cola_prioridad = []
    es_pila = es_cola = es_cola_prioridad = True

    for tipo, x in comandos:
        if tipo == 1:
            # Insertar en todas las estructuras
            pila.append(x)
            cola.append(x)
            heapq.heappush(cola_prioridad, -x)  # Insertamos el valor negativo para simular una cola de prioridad máxima
        elif tipo == 2:
            if es_pila:
                # Verificamos si cumple con la pila
                if pila and pila[-1] == x:
                    pila.pop()
                else:
                    es_pila = False

            if es_cola:
                # Verificamos si cumple con la cola
                if cola and cola[0] == x:
                    cola.pop(0)
                else:
                    es_cola = False

            if es_cola_prioridad:
                # Verificamos si cumple con la cola de prioridad
                if cola_prioridad and -cola_prioridad[0] == x:
                    heapq.heappop(cola_prioridad)
                else:
                    es_cola_prioridad = False

    # Determinamos el resultado basado en las estructuras válidas
    if es_pila + es_cola + es_cola_prioridad > 1:
        return "not sure"
    elif es_pila:
        return "stack"
    elif es_cola:
        return "queue"
    elif es_cola_prioridad:
        return "priority queue"
    else:
        return "impossible"

# Procesar múltiples casos de prueba hasta EOF
resultados = []
try:
    while True:
        # Leer la cantidad de operaciones para el caso de prueba
        linea = input().strip()
        if not linea:
            break
        n = int(linea)
        comandos = []
        
        # Leer cada comando para el caso de prueba
        for _ in range(n):
            tipo, x = map(int, input().strip().split())
            comandos.append((tipo, x))
        
        # Determinar el tipo de estructura y almacenar el resultado
        resultados.append(determinar_estructura(comandos))
except EOFError:
    pass

# Imprimir todos los resultados de cada caso de prueba
print("\n".join(resultados))

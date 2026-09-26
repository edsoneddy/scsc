import sys
import heapq

def identificar_estructura(operaciones):
    pila_simulada = []
    cola_simulada = []
    cola_prioritaria_simulada = []
    
    es_tipo_pila = True
    es_tipo_cola = True
    es_tipo_cola_prioritaria = True

    for operacion in operaciones:
        accion, valor = operacion
        
        if accion == 1:  # Insertar
            pila_simulada.append(valor)
            cola_simulada.append(valor)
            heapq.heappush(cola_prioritaria_simulada, -valor) 
        
        elif accion == 2:  # Extraer
            if es_tipo_pila:
                if not pila_simulada or pila_simulada.pop() != valor:
                    es_tipo_pila = False
            if es_tipo_cola:
                if not cola_simulada or cola_simulada.pop(0) != valor:
                    es_tipo_cola = False
            if es_tipo_cola_prioritaria:
                if not cola_prioritaria_simulada or -heapq.heappop(cola_prioritaria_simulada) != valor:
                    es_tipo_cola_prioritaria = False

    total_posibilidades = sum([es_tipo_pila, es_tipo_cola, es_tipo_cola_prioritaria])
    if total_posibilidades == 0:
        return "impossible"
    elif total_posibilidades > 1:
        return "not sure"
    elif es_tipo_pila:
        return "stack"
    elif es_tipo_cola:
        return "queue"
    elif es_tipo_cola_prioritaria:
        return "priority queue"

# Leer entrada
datos = sys.stdin.read().strip().split("\n")
indice = 0
respuestas = []

while indice < len(datos):
    cantidad = int(datos[indice])
    indice += 1
    lista_operaciones = []
    for _ in range(cantidad):
        instruccion = list(map(int, datos[indice].split()))
        lista_operaciones.append(instruccion)
        indice += 1
    respuestas.append(identificar_estructura(lista_operaciones))

# Imprimir resultados
print("\n".join(respuestas))

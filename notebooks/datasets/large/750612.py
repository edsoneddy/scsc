import sys
import heapq

def identificar_estructura(operaciones):
    es_pila = True
    es_cola = True
    es_cola_prioridad = True

    pila = []
    cola = []
    cola_prioridad = []

    for operacion in operaciones:
        tipo, x = operacion

        if tipo == 1:  # Operación de inserción
            pila.append(x)
            cola.append(x)
            heapq.heappush(cola_prioridad, -x)  # Usamos valores negativos para simular max-heap
        elif tipo == 2:  # Operación de extracción
            if es_pila:
                if pila and pila[-1] == x:
                    pila.pop()
                else:
                    es_pila = False
            if es_cola:
                if cola and cola[0] == x:
                    cola.pop(0)
                else:
                    es_cola = False
            if es_cola_prioridad:
                if cola_prioridad and -cola_prioridad[0] == x:
                    heapq.heappop(cola_prioridad)
                else:
                    es_cola_prioridad = False

    # Determinar el resultado final
    if es_pila and not es_cola and not es_cola_prioridad:
        return "stack"
    elif es_cola and not es_pila and not es_cola_prioridad:
        return "queue"
    elif es_cola_prioridad and not es_pila and not es_cola:
        return "priority queue"
    elif es_pila or es_cola or es_cola_prioridad:
        return "not sure"
    else:
        return "impossible"

def main():
    input = sys.stdin.read()
    data = input.strip().splitlines()
    idx = 0

    resultados = []
    while idx < len(data):
        n = int(data[idx])
        idx += 1
        operaciones = []
        for _ in range(n):
            tipo, x = map(int, data[idx].split())
            operaciones.append((tipo, x))
            idx += 1
        resultados.append(identificar_estructura(operaciones))

    print("\n".join(resultados))

if __name__ == "__main__":
    main()

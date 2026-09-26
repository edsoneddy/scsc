import sys
import heapq

def procesar_caso(n, operaciones):
    es_pila = True
    es_cola = True
    es_cola_prioridad = True
    
    pila = []
    cola = []
    cola_prioridad = []
    
    for operacion in operaciones:
        tipo, valor = operacion
        
        if tipo == 1:
            pila.append(valor)
            cola.append(valor)
            heapq.heappush(cola_prioridad, -valor)
        
        elif tipo == 2:
            if es_pila:
                if not pila or pila[-1] != valor:
                    es_pila = False
                else:
                    pila.pop()
            
            if es_cola:
                if not cola or cola[0] != valor:
                    es_cola = False
                else:
                    cola.pop(0)
            
            if es_cola_prioridad:
                if not cola_prioridad or -cola_prioridad[0] != valor:
                    es_cola_prioridad = False
                else:
                    heapq.heappop(cola_prioridad)
    
    if es_pila + es_cola + es_cola_prioridad == 0:
        return "impossible"
    elif es_pila + es_cola + es_cola_prioridad > 1:
        return "not sure"
    elif es_pila:
        return "stack"
    elif es_cola:
        return "queue"
    elif es_cola_prioridad:
        return "priority queue"

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    resultados = []
    
    while index < len(data):
        n = int(data[index])
        index += 1
        operaciones = []
        
        for _ in range(n):
            tipo = int(data[index])
            valor = int(data[index + 1])
            operaciones.append((tipo, valor))
            index += 2
        
        resultado = procesar_caso(n, operaciones)
        resultados.append(resultado)
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()
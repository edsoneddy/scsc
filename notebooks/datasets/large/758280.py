from collections import deque
import sys
import heapq

def resolver_estructuras():
    input = sys.stdin.read
    datos = input().strip().split("\n")
    i = 0

    resultados = []
    
    while i < len(datos):
        n = int(datos[i])  
        i += 1
        
        pila = []  
        cola = deque()  
        cola_prioridad = []  
        
        es_pila = True
        es_cola = True
        es_cola_prioridad = True
        
        for _ in range(n):
            comando, x = map(int, datos[i].split())
            i += 1
            
            if comando == 1:
                if es_pila:
                    pila.append(x)
                if es_cola:
                    cola.append(x)
                if es_cola_prioridad:
                    heapq.heappush(cola_prioridad, -x)  
            elif comando == 2:
                if es_pila:
                    if pila and pila[-1] == x:
                        pila.pop()
                    else:
                        es_pila = False
                if es_cola:
                    if cola and cola[0] == x:
                        cola.popleft()
                    else:
                        es_cola = False
                if es_cola_prioridad:
                    if cola_prioridad and -heapq.heappop(cola_prioridad) == x:
                        pass
                    else:
                        es_cola_prioridad = False

        opciones = sum([es_pila, es_cola, es_cola_prioridad])
        if opciones > 1:
            resultados.append("not sure")
        elif es_pila:
            resultados.append("stack")
        elif es_cola:
            resultados.append("queue")
        elif es_cola_prioridad:
            resultados.append("priority queue")
        else:
            resultados.append("impossible")

    for resultado in resultados:
        print(resultado)


if __name__ == "__main__":
    resolver_estructuras()
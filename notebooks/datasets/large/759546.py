from collections import deque
import heapq
import sys

def determinar_estructura(casos):
    resultados = []
    
    for caso in casos:
        n, operaciones = caso
        es_pila, es_cola, es_cola_prioridad = True, True, True
        pila, cola, cola_prioridad = [], deque(), []
        
        for operacion in operaciones:
            tipo, x = operacion
            
            if tipo == 1:  # Operación de inserción
                pila.append(x)
                cola.append(x)
                heapq.heappush(cola_prioridad, -x)  # Usamos valores negativos para simular cola de prioridad max
        
            elif tipo == 2:  # Operación de extracción
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
                    if cola_prioridad and -cola_prioridad[0] == x:
                        heapq.heappop(cola_prioridad)
                    else:
                        es_cola_prioridad = False
        
        # Decidir el resultado para este caso
        posibles = sum([es_pila, es_cola, es_cola_prioridad])
        if posibles > 1:
            resultados.append("not sure")
        elif es_pila:
            resultados.append("stack")
        elif es_cola:
            resultados.append("queue")
        elif es_cola_prioridad:
            resultados.append("priority queue")
        else:
            resultados.append("impossible")
    
    return resultados


# Procesar entrada
def procesar_entrada():
    casos = []
    entrada = sys.stdin.read().strip().split("\n")
    i = 0
    while i < len(entrada):
        n = int(entrada[i])
        i += 1
        operaciones = []
        for _ in range(n):
            tipo, x = map(int, entrada[i].split())
            operaciones.append((tipo, x))
            i += 1
        casos.append((n, operaciones))
    return casos


# Leer entrada y generar salida
if __name__ == "__main__":
    casos = procesar_entrada()
    resultados = determinar_estructura(casos)
    for resultado in resultados:
        print(resultado)
 
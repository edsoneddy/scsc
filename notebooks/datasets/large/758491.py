import sys
import heapq

def principal():
    entrada = sys.stdin.read
    datos = entrada().strip().splitlines()
    
    indice = 0
    resultados = []
    
    while indice < len(datos):
        n = int(datos[indice])
        indice += 1
        
        pila = []
        cola = []
        cola_prioridad = []
        es_pila = True
        es_cola = True
        es_cola_prioridad = True
        
        for _ in range(n):
            comando = datos[indice].split()
            indice += 1
            operacion = int(comando[0])
            if operacion == 1:
                x = int(comando[1])
                pila.append(x)
                cola.append(x)
                heapq.heappush(cola_prioridad, -x)
            elif operacion == 2:
                x = int(comando[1])
                
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
        
        conteo_valido = es_pila + es_cola + es_cola_prioridad
        
        if conteo_valido == 0:
            resultados.append("impossible")
        elif conteo_valido > 1:
            resultados.append("not sure")
        else:
            if es_pila:
                resultados.append("stack")
            elif es_cola:
                resultados.append("queue")
            elif es_cola_prioridad:
                resultados.append("priority queue")
    
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    principal()

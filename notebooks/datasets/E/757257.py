import heapq

def adivinar_estructura():
    while True:
        try:
            
            n = int(input())
            
           
            pila = []
            cola = []
            cola_prioridad = []
            
           
            es_pila = True
            es_cola = True
            es_cola_prioridad = True
            
            for _ in range(n):
               
                op, x = map(int, input().split())
                
                if op == 1:
                    
                    pila.append(x)
                    cola.append(x)
                    heapq.heappush(cola_prioridad, -x)  
                else:
                    
                    if not pila or pila.pop() != x:
                        es_pila = False
                    
                    
                    if not cola or cola.pop(0) != x:
                        es_cola = False
                    
                    
                    if not cola_prioridad or -heapq.heappop(cola_prioridad) != x:
                        es_cola_prioridad = False
            
            
            estructuras = []
            if es_pila:
                estructuras.append('stack')
            if es_cola:
                estructuras.append('queue')
            if es_cola_prioridad:
                estructuras.append('priority queue')
            
            
            if len(estructuras) > 1:
                print('not sure')
            elif len(estructuras) == 1:
                print(estructuras[0])
            else:
                print('impossible')
        
        except EOFError:
            break

# Ejecutar la solución
adivinar_estructura()

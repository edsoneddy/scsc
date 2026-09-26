from queue import PriorityQueue

def evaluar_estructura(cantidad, secuencia):
    pila_valida = True
    cola_valida = True
    cola_prioridad_valida = True
    
    pila = []
    cola = []
    cola_prioridad = PriorityQueue()
    
    for operacion in secuencia:
        tipo, valor = operacion
        if tipo == 1:
            if pila_valida:
                pila.append(valor)
            if cola_valida:
                cola.append(valor)
            if cola_prioridad_valida:
                cola_prioridad.put(-valor)
        elif tipo == 2:
            if pila_valida:
                if pila and pila[-1] == valor:
                    pila.pop()
                else:
                    pila_valida = False
            if cola_valida:
                if cola and cola[0] == valor:
                    cola.pop(0)
                else:
                    cola_valida = False
            if cola_prioridad_valida:
                if not cola_prioridad.empty() and -cola_prioridad.get() == valor:
                    pass
                else:
                    cola_prioridad_valida = False
    
    if pila_valida + cola_valida + cola_prioridad_valida > 1:
        return "not sure"
    elif pila_valida:
        return "stack"
    elif cola_valida:
        return "queue"
    elif cola_prioridad_valida:
        return "priority queue"
    else:
        return "impossible"

while True:
    try:
        cantidad = int(input())
        secuencia = []
        for _ in range(cantidad):
            comando = list(map(int, input().split()))
            secuencia.append(comando)
        print(evaluar_estructura(cantidad, secuencia))
    except EOFError:
        break

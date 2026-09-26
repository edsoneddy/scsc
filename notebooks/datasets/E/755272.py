import sys
import queue

def verificar_estructura(comandos):
    stack = []
    queue = []
    priority_queue = []

    es_stack = True
    es_queue = True
    es_priority_queue = True

    for comando, valor in comandos:
        if comando == 1:
            stack.append(valor)
            queue.append(valor)
            priority_queue.append(valor)
            priority_queue.sort(reverse=True)  
        else:
            if es_stack:
                if not stack or stack.pop() != valor:
                    es_stack = False
            if es_queue:
                if not queue or queue.pop(0) != valor:
                    es_queue = False
            if es_priority_queue:
                if not priority_queue or priority_queue.pop(0) != valor:
                    es_priority_queue = False

    if es_stack + es_queue + es_priority_queue == 0:
        return "impossible"
    elif es_stack + es_queue + es_priority_queue > 1:
        return "not sure"
    else:
        if es_stack:
            return "stack"
        elif es_queue:
            return "queue"
        elif es_priority_queue:
            return "priority queue"

def main():
    input = sys.stdin.read
    data = input().split()
    index = 0

    while index < len(data):
        n = int(data[index])
        index += 1
        comandos = []
        
        for _ in range(n):
            comando = int(data[index])
            valor = int(data[index + 1])
            comandos.append((comando, valor))
            index += 2
        
        resultado = verificar_estructura(comandos)
        print(resultado)

if __name__ == "__main__":
    main()

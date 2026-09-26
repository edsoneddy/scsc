from collections import deque
import heapq


def main():
    try:
        while True:
            # Verificar si la entrada está vacía antes de procesarla
            line = input().strip()
            if not line:  # Si la línea está vacía, se ignora
                continue

            n = int(line)  # Número de operaciones
            pila = []
            cola = deque()
            cola_prioridad = []
            is_pila = True
            is_cola = True
            is_cola_prioridad = True

            for _ in range(n):
                # Leer una línea con múltiples valores
                datos = input().strip().split()  # Separar la línea por espacios
                if not datos:  # Si la línea está vacía, saltarla
                    continue
                tipo = int(datos[0])  # Tipo de operación
                if tipo == 1:  # Inserción
                    x = int(datos[1])  # Elemento a insertar
                    pila.append(x)
                    cola.append(x)
                    heapq.heappush(cola_prioridad,
                                   -x)  # Usamos heapq para la cola de prioridad (invertimos el signo para obtener el máximo)
                elif tipo == 2:
                    x = int(datos[1])  # Elemento a verificar
                    if is_pila:
                        if not pila or pila.pop() != x:
                            is_pila = False
                    if is_cola:
                        if not cola or cola.popleft() != x:
                            is_cola = False
                    if is_cola_prioridad:
                        if not cola_prioridad or -heapq.heappop(cola_prioridad) != x:
                            is_cola_prioridad = False

            count = 0
            if is_pila:
                count += 1
            if is_cola:
                count += 1
            if is_cola_prioridad:
                count += 1

            if count == 0:
                print("impossible")
            elif count > 1:
                print("not sure")
            else:
                if is_pila:
                    print("stack")
                elif is_cola:
                    print("queue")
                elif is_cola_prioridad:
                    print("priority queue")
    except EOFError:
        pass  # Cuando el fin de archivo es alcanzado, se detiene el ciclo.


if __name__ == "__main__":
    main()

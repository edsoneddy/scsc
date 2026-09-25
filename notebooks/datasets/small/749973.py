import heapq
import sys

def main():
    max_heap = []
    results = []
    input = sys.stdin.read().strip().splitlines()

    for line in input:
        parts = line.split()
        command = parts[0]

        if command == "S":
            # Guardar una copia del número x (como valor negativo para el max-heap)
            x = int(parts[1])
            heapq.heappush(max_heap, -x)

        elif command == "A":
            # Imprimir el número más grande
            if max_heap:
                results.append(-max_heap[0])
            else:
                results.append("Error")

        elif command == "R":
            # Extraer el número más grande
            if max_heap:
                heapq.heappop(max_heap)
            else:
                results.append("Error")

        elif command == "I":
            # Incrementar el número más grande en x
            if max_heap:
                x = int(parts[1])
                max_value = -heapq.heappop(max_heap)
                heapq.heappush(max_heap, -(max_value + x))
            else:
                results.append("Error")

        elif command == "D":
            # Decrementar el número más grande en x
            if max_heap:
                x = int(parts[1])
                max_value = -heapq.heappop(max_heap)
                heapq.heappush(max_heap, -(max_value - x))
            else:
                results.append("Error")

        elif command == "T":
            # Termina la entrada
            break

    # Imprimir todos los resultados acumulados
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()

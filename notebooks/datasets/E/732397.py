def dot_product(vector_a, vector_b):
    """Calcula el producto escalar de dos vectores."""
    return sum(a * b for a, b in zip(vector_a, vector_b))

def main():
    import sys
    
    input_data = sys.stdin.read().strip().splitlines()
    num_cases = int(input_data[0])
    
    results = []
    index = 1
    for _ in range(num_cases):
        n = int(input_data[index])  # Leer el tamaño del vector
        vector_a = list(map(int, input_data[index + 1].split()))  # Leer el vector A
        vector_b = list(map(int, input_data[index + 2].split()))  # Leer el vector B
        index += 3
        
        # Calcular el producto escalar
        product = dot_product(vector_a, vector_b)
        results.append(product)
    
    # Imprimir los resultados
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

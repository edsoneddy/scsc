from collections import deque

def generar_parentesis_con_cola(n):
    
    cola = deque([("(", 1, 0)])
    secuencias = []

    while cola:
        secuencia, abiertos, cerrados = cola.popleft()

        
        if len(secuencia) == 2 * n:
            secuencias.append(secuencia)
            continue

        
        if abiertos < n:
            cola.append((secuencia + '(', abiertos + 1, cerrados))

        
        if cerrados < abiertos:
            cola.append((secuencia + ')', abiertos, cerrados + 1))

    return secuencias

def main():
    import sys
    input = sys.stdin.read
    datos = input().strip().split()
    
    resultados = []
    for caso in datos:
        n = int(caso)
        secuencias = generar_parentesis_con_cola(n)
        resultados.extend(secuencias)
        

    print("\n".join(resultados).strip())

if __name__ == "__main__":
    main()

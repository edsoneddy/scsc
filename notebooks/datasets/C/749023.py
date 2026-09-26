def generar_parantesis(n):
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            resultados.append(current)
            return
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    resultados = []
    backtrack('', 0, 0)
    return resultados

def main():
    import sys
    for line in sys.stdin:
        n = int(line.strip())
        resultados = generar_parantesis(n)
        for secuencia in resultados:
            print(secuencia)

if __name__ == "__main__":
    main()

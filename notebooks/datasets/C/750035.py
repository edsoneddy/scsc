def generar_parentesis(n):
    def backtrack(abiertos, cerrados, actual):

        if abiertos == 0 and cerrados == 0:
            resultado.append(actual)
            return

        if abiertos > 0:
            backtrack(abiertos - 1, cerrados + 1, actual + "(")

        if cerrados > 0:
            backtrack(abiertos, cerrados - 1, actual + ")")
    
    resultado = []
    backtrack(n, 0, "")
    return resultado

def main():
    while True:
        try:
            n = int(input())
            secuencias = generar_parentesis(n)
            for secuencia in secuencias:
                print(secuencia)
        except EOFError:
            break

if __name__ == "__main__":  
    main()

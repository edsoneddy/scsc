def generar_parentesis(n, abiertos, cerrados, secuencia, resultado):
    if len(secuencia) == 2 * n:
        resultado.append(secuencia)
        return
    
    if abiertos < n:
        generar_parentesis(n, abiertos + 1, cerrados, secuencia + '(', resultado)
    
    if cerrados < abiertos:
        generar_parentesis(n, abiertos, cerrados + 1, secuencia + ')', resultado)

def main():
    import sys
    input = sys.stdin.read().strip().splitlines()
    for linea in input:
        if linea:
            n = int(linea)
            resultado = []
            generar_parentesis(n, 0, 0, "", resultado)
            print("\n".join(resultado))

if __name__ == "__main__":
    main()

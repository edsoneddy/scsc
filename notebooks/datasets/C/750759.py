def generar_parentesis(n):
    generar_parentesis_recursivo("", 0, 0, n)

def generar_parentesis_recursivo(secuencia, abiertos, cerrados, n):
    if len(secuencia) == 2 * n:
        print(secuencia)
        return
    if abiertos < n:
        generar_parentesis_recursivo(secuencia + "(", abiertos + 1, cerrados, n)
    if cerrados < abiertos:
        generar_parentesis_recursivo(secuencia + ")", abiertos, cerrados + 1, n)

if __name__ == "__main__":
    try:
        while True:
            n = int(input().strip())
            generar_parentesis(n)
    except EOFError:
        pass

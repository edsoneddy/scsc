def generar_parentesis(abiertos, cerrados, secuencia, n, resultado):
    if len(secuencia) == 2 * n:
        resultado.append(secuencia)
        return

    if abiertos < n:
        generar_parentesis(abiertos + 1, cerrados, secuencia + '(', n, resultado)

    if cerrados < abiertos:
        generar_parentesis(abiertos, cerrados + 1, secuencia + ')', n, resultado)


def resolver(n):
    resultado = []
    generar_parentesis(0, 0, '', n, resultado)
    for secuencia in resultado:
        print(secuencia)


def main():
    try:
        while True:
            entrada = input().strip()
            if entrada:
                n = int(entrada)
                resolver(n)
    except EOFError:
        pass


if __name__ == "__main__":
    main()

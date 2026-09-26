def main():
    import sys
    for line in sys.stdin:
        pares = int(line.strip())
        secuencias = []
        construir_secuencias("", 0, 0, pares, secuencias)
        for s in secuencias:
            print(s)

def construir_secuencias(actual, abiertos, cerrados, limite, secuencias):
    if len(actual) == 2 * limite:
        secuencias.append(actual)
        return
    if abiertos < limite:
        construir_secuencias(actual + "(", abiertos + 1, cerrados, limite, secuencias)
    if cerrados < abiertos:
        construir_secuencias(actual + ")", abiertos, cerrados + 1, limite, secuencias)

if __name__ == "__main__":
    main()

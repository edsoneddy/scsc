def generar_parentesis(sec_actual, abiertos, cerrados, n):
    if len(sec_actual) == 2 * n:
        print(sec_actual)
        return

    if abiertos < n:
        generar_parentesis(sec_actual + '(', abiertos + 1, cerrados, n)
    
    if cerrados < abiertos:
        generar_parentesis(sec_actual + ')', abiertos, cerrados + 1, n)

def main():
    try:
        while True:
            n = int(input().strip())
            generar_parentesis('', 0, 0, n)
    except EOFError:
        pass

if __name__ == "__main__":
    main()

def generar_parentesis(n, abiertos=0, cerrados=0, secuencia=''):
    if len(secuencia) == 2 * n:
        print(secuencia)
        return
    if abiertos < n:
        generar_parentesis(n, abiertos + 1, cerrados, secuencia + '(')
    if cerrados < abiertos:
        generar_parentesis(n, abiertos, cerrados + 1, secuencia + ')')
def main():
    try:
        while True:
            n = int(input())
            generar_parentesis(n)
    except EOFError:
        pass
main()
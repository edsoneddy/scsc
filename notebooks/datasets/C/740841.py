def generar_parentesis(n, abiertos=0, cerrados=0, secuencia=""):
    if abiertos == n and cerrados == n:
        print(secuencia)
        return
    if abiertos < n:
        generar_parentesis(n, abiertos + 1, cerrados, secuencia + '(')
    if cerrados < abiertos:
        generar_parentesis(n, abiertos, cerrados + 1, secuencia + ')')

while True:
    try:
        n = int(input())
        generar_parentesis(n)
    except EOFError:
        break

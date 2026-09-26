def generar_parentesis(n, abiertos, cerrados, secuencia, resultado):
    if len(secuencia) == 2 * n:
        resultado.append(secuencia)
        return

    if abiertos < n:
        generar_parentesis(n, abiertos + 1, cerrados, secuencia + '(', resultado)

    if cerrados < abiertos:
        generar_parentesis(n, abiertos, cerrados + 1, secuencia + ')', resultado)

def secuencias_parentesis(n):
    resultado = []
    generar_parentesis(n, 0, 0, '', resultado)
    return resultado

while True:
    try:
        n = int(input())
        
        secuencias = secuencias_parentesis(n)
        for secuencia in secuencias:
            print(secuencia)
    except EOFError:
        break
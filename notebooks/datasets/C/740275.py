def generar_parentesis(n, apertura, cierre, secuencia):
    if len(secuencia) == 2 * n:
        print(secuencia)
        return
    
    if apertura < n:
        generar_parentesis(n, apertura + 1, cierre, secuencia + "(")
    
    if cierre < apertura:
        generar_parentesis(n, apertura, cierre + 1, secuencia + ")")

while True:
    try:
        n = int(input().strip())
        generar_parentesis(n, 0, 0, "")
    except EOFError:
        break

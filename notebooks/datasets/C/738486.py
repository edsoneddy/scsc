def generar_parentesis(n, apertura=0, cierre=0, secuencia="", resultado=None):
    if resultado is None:
        resultado = []
    
    if len(secuencia) == 2 * n:
        resultado.append(secuencia)
        return
    
    if apertura < n:
        generar_parentesis(n, apertura + 1, cierre, secuencia + "(", resultado)
    
    if cierre < apertura:
        generar_parentesis(n, apertura, cierre + 1, secuencia + ")", resultado)
    
    return resultado

def imprimir_secuencias(n):
    secuencias = generar_parentesis(n)
    for secuencia in secuencias:
        print(secuencia)

# Leer múltiples casos de prueba
import sys
for line in sys.stdin:
    n = int(line.strip())
    imprimir_secuencias(n)

def generar_parentesis(n, abiertos, cerrados, secuencia, resultado):
    if len(secuencia) == 2 * n:
        resultado.append(secuencia)
        return
    
    if abiertos < n:
        generar_parentesis(n, abiertos + 1, cerrados, secuencia + "(", resultado)
    
    if cerrados < abiertos:
        generar_parentesis(n, abiertos, cerrados + 1, secuencia + ")", resultado)

# Leer la entrada hasta EOF
import sys
input = sys.stdin.read

datos = input().split()

for caso in datos:
    n = int(caso)
    resultado = []
    generar_parentesis(n, 0, 0, "", resultado)
    
    for secuencia in resultado:
        print(secuencia)

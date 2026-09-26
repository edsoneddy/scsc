def generar_secuencias(n, secuencia="", abiertos=0, cerrados=0):
    if len(secuencia) == 2 * n:
        print(secuencia)
        return  
    if abiertos < n:
        generar_secuencias(n, secuencia + "(", abiertos + 1, cerrados)  
    if cerrados < abiertos:
        generar_secuencias(n, secuencia + ")", abiertos, cerrados + 1)
import sys
input = sys.stdin.read
data = input().splitlines()
for linea in data:
    if linea:
        n = int(linea)
        generar_secuencias(n)
def generar_parentesis(n, abiertos=0, cerrados=0, secuencia=""):
    # Si la secuencia tiene la longitud 2n, la imprimimos
    if len(secuencia) == 2 * n:
        print(secuencia)
        return

    # Intentamos agregar un paréntesis abierto si es posible
    if abiertos < n:
        generar_parentesis(n, abiertos + 1, cerrados, secuencia + "(")

    # Intentamos agregar un paréntesis cerrado si es posible
    if cerrados < abiertos:
        generar_parentesis(n, abiertos, cerrados + 1, secuencia + ")")

# Leer múltiples casos de prueba hasta que no haya más entradas
import sys
for linea in sys.stdin:
    n = int(linea.strip())
    generar_parentesis(n)
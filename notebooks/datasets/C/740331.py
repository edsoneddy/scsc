# Función recursiva para generar secuencias válidas de paréntesis
def generar_parentesis(abiertos, cerrados, secuencia, n, resultado):
    if len(secuencia) == 2 * n:  # Si la secuencia tiene la longitud correcta
        resultado.append(secuencia)
        return
    
    if abiertos < n:  # Si podemos añadir más paréntesis abiertos
        generar_parentesis(abiertos + 1, cerrados, secuencia + '(', n, resultado)
    
    if cerrados < abiertos:  # Si podemos añadir más paréntesis cerrados
        generar_parentesis(abiertos, cerrados + 1, secuencia + ')', n, resultado)

# Función principal para manejar la entrada y salida
def imprimir_todas_las_secuencias(n):
    resultado = []
    generar_parentesis(0, 0, "", n, resultado)
    for secuencia in resultado:
        print(secuencia)

# Leer múltiples casos de prueba hasta que no haya más datos
import sys
for linea in sys.stdin:
    n = int(linea.strip())
    imprimir_todas_las_secuencias(n)

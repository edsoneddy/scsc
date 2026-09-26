def generar_parentesis(n):
    resultados = []
    
    def backtrack(s='', abiertos=0, cerrados=0):
        if len(s) == 2 * n:  # Si la secuencia está completa
            resultados.append(s)
            return
        if abiertos < n:  # Añadir un paréntesis abierto si no hemos alcanzado el límite
            backtrack(s + '(', abiertos + 1, cerrados)
        if cerrados < abiertos:  # Añadir un paréntesis cerrado si es válido
            backtrack(s + ')', abiertos, cerrados + 1)
    
    backtrack()
    return resultados

# Leer la entrada de varios casos de prueba
import sys
input = sys.stdin.read

# Procesar cada caso de prueba
for linea in input().strip().split():
    n = int(linea)
    secuencias = generar_parentesis(n)
    print("\n".join(secuencias))


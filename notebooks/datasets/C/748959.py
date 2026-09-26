def generar_parentesis(n):
    def backtrack(combinacion, abiertos, cerrados):
        # Si hemos alcanzado el tamaño de 2 * n, guardamos la combinación
        if len(combinacion) == 2 * n:
            resultado.append("".join(combinacion))
            return
        
        # Agregar un paréntesis abierto si hay menos de n
        if abiertos < n:
            combinacion.append('(')
            backtrack(combinacion, abiertos + 1, cerrados)
            combinacion.pop()
        
        # Agregar un paréntesis cerrado si hay menos cerrados que abiertos
        if cerrados < abiertos:
            combinacion.append(')')
            backtrack(combinacion, abiertos, cerrados + 1)
            combinacion.pop()

    resultado = []
    backtrack([], 0, 0)
    return resultado

# Lectura de entrada y ejecución para cada caso
import sys
input = sys.stdin.read
entradas = input().strip().split()

for entrada in entradas:
    n = int(entrada)
    combinaciones = generar_parentesis(n)
    for combinacion in combinaciones:
        print(combinacion)

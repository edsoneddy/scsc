def generar_parentesis(n):
    # Función recursiva para generar paréntesis
    def backtrack(s, abiertos, cerrados):
        # Si la longitud de la secuencia es 2n, es válida
        if len(s) == 2 * n:
            print(s)
            return
        # Si aún podemos agregar un paréntesis abierto
        if abiertos < n:
            backtrack(s + '(', abiertos + 1, cerrados)
        # Si podemos agregar un paréntesis cerrado (debe haber abiertos disponibles)
        if cerrados < abiertos:
            backtrack(s + ')', abiertos, cerrados + 1)

    # Iniciar el proceso con la secuencia vacía
    backtrack('', 0, 0)

# Lectura de la entrada sin sys
while True:
    try:
        n = int(input().strip())  # Lee el número n para cada caso de prueba
        generar_parentesis(n)
    except EOFError:  # Termina cuando no haya más entradas
        break

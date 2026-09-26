def generar_parentesis(n):
    resultados = []

    def backtrack(secuencia, aperturas, cierres):
        # Si la secuencia tiene la longitud de 2n, la agregamos a los resultados
        if len(secuencia) == 2 * n:
            resultados.append(secuencia)
            return
        # Agregar un paréntesis de apertura si no hemos alcanzado el máximo permitido
        if aperturas < n:
            backtrack(secuencia + '(', aperturas + 1, cierres)
        # Agregar un paréntesis de cierre si no se supera el número de aperturas
        if cierres < aperturas:
            backtrack(secuencia + ')', aperturas, cierres + 1)

    # Llamamos al backtracking con una secuencia vacía
    backtrack('', 0, 0)
    return resultados

# Entrada de datos
try:
    while True:
        linea = input().strip()
        if not linea:
            break
        n = int(linea)
        secuencias = generar_parentesis(n)
        # Imprimir cada secuencia en una nueva línea
        for secuencia in secuencias:
            print(secuencia)
except EOFError:
    pass


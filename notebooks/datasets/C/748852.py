def generar_secuencias(n, secuencia='', izq=0, der=0):
    if izq + der == 2 * n:
        print(secuencia)
    if izq < n:
        generar_secuencias(n, secuencia + '(', izq + 1, der)
    if der < izq:
        generar_secuencias(n, secuencia + ')', izq, der + 1)

while True:
    try:
        n = int(input())
        generar_secuencias(n)
    except EOFError:
        break
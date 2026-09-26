def genera_secuencias(n, secuencia='', izq=0, der=0):
    if izq + der == 2 * n:
        print(secuencia)
    if izq < n:
        genera_secuencias(n, secuencia + '(', izq + 1, der)
    if der < izq:
        genera_secuencias(n, secuencia + ')', izq, der + 1)

while True:
    try:
        n = int(input())
        genera_secuencias(n)
    except EOFError:
        break
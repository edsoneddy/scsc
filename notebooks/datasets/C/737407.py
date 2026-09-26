def generar_secuencias(n, secuencia='', a=0, c=0):
    if len(secuencia) == 2 * n:
        print(secuencia)
        return
    if a < n:
        generar_secuencias(n, secuencia + '(', a + 1, c)
    if c < a:
        generar_secuencias(n, secuencia + ')', a, c + 1)

while True:
    try:
        n = int(input())
        generar_secuencias(n)
    except EOFError:
        break

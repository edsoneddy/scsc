def generar_paracentesis(n, abierto=0, cerrado=0, secuencia=''):
    if abierto + cerrado == 2 * n:
        print(secuencia)
        return
    if abierto < n:
        generar_paracentesis(n, abierto + 1, cerrado, secuencia + '(')
    if cerrado < abierto:
        generar_paracentesis(n, abierto, cerrado + 1, secuencia + ')')

# Lectura de la entrada
while True:
    try:
        n = int(input())
        generar_paracentesis(n)
    except EOFError:
        break

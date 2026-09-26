def generar_parentesis(n):
    resultado = []
    pila = [("", 0, 0)]  

    while pila:
        secuencia, abiertos, cerrados = pila.pop()
        if len(secuencia) == 2 * n:
            resultado.append(secuencia)
            continue

        if abiertos < n:
            pila.append((secuencia + "(", abiertos + 1, cerrados))

        if cerrados < abiertos:
            pila.append((secuencia + ")", abiertos, cerrados + 1))

    return sorted(resultado)

while True:
    try:
        n = int(input())
        secuencias = generar_parentesis(n)
        for secuencia in secuencias:
            print(secuencia)
    except EOFError:
        break
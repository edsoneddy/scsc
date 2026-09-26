def generar_parentesis(abiertos, cerrados, n, secuencia):
    # Si hemos colocado n paréntesis abiertos y n cerrados, la secuencia es válida y completa.
    if abiertos == n and cerrados == n:
        print(secuencia)
        return

    # Podemos añadir un paréntesis abierto si aún no hemos añadido n abiertos
    if abiertos < n:
        generar_parentesis(abiertos + 1, cerrados, n, secuencia + "(")

    # Podemos añadir un paréntesis cerrado si hemos añadido menos cerrados que abiertos
    if cerrados < abiertos:
        generar_parentesis(abiertos, cerrados + 1, n, secuencia + ")")

# Leer los casos de prueba
try:
    while True:
        entrada = input().strip()
        if entrada == "":
            break
        n = int(entrada)
        # Generar todas las secuencias de paréntesis válidas para el valor de n dado
        generar_parentesis(0, 0, n, "")
except EOFError:
    pass
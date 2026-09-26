def generar_parentesis(n, abiertos=0, cerrados=0, secuencia=""):
    # Si hemos generado una secuencia de longitud 2n, la imprimimos
    if len(secuencia) == 2 * n:
        print(secuencia)
        return
    
    # Intentamos agregar un paréntesis abierto si aún no hemos usado todos
    if abiertos < n:
        generar_parentesis(n, abiertos + 1, cerrados, secuencia + "(")
    
    # Intentamos agregar un paréntesis cerrado si es posible
    if cerrados < abiertos:
        generar_parentesis(n, abiertos, cerrados + 1, secuencia + ")")

try:
    while True:
        # Leemos el valor de n desde la entrada
        n = int(input().strip())
        generar_parentesis(n)
except EOFError:
    pass
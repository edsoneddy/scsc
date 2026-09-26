def crear_combinaciones_parentesis(n, combinacion_actual="", conteo_abiertos=0, conteo_cerrados=0):
    if len(combinacion_actual) == 2 * n:
        print(combinacion_actual)
        return
    if conteo_abiertos < n:
        crear_combinaciones_parentesis(n, combinacion_actual + '(', conteo_abiertos + 1, conteo_cerrados)
    if conteo_cerrados < conteo_abiertos:
        crear_combinaciones_parentesis(n, combinacion_actual + ')', conteo_abiertos, conteo_cerrados + 1)

def iniciar():
    try:
        while True:
            cantidad = int(input().strip())
            crear_combinaciones_parentesis(cantidad)
    except EOFError:
        pass

if __name__ == "__main__":
    iniciar()

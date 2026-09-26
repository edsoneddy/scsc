def generar_parentesis(n, abiertos=0, cerrados=0, secuencia="", resultados=[]):
    """Genera todas las combinaciones válidas de paréntesis."""
    if len(secuencia) == 2 * n:
        resultados.append(secuencia)
        return

    if abiertos < n:
        generar_parentesis(n, abiertos + 1, cerrados, secuencia + "(", resultados)
    if cerrados < abiertos:
        generar_parentesis(n, abiertos, cerrados + 1, secuencia + ")", resultados)

def main():
    import sys
    input = sys.stdin.read
    datos = input().splitlines()
    
    for linea in datos:
        if linea.strip():  
            n = int(linea)
            resultados = []
            generar_parentesis(n, resultados=resultados)
            for secuencia in resultados:
                print(secuencia)

if __name__ == "__main__":
    main()

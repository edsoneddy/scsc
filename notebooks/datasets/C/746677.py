def generar_secuencias(n):
    def generar_recursivo(abiertos, cerrados, secuencia_actual, secuencias):
        if abiertos == n and cerrados == n:
            secuencias.append(secuencia_actual)
            return
        if abiertos < n:
            generar_recursivo(abiertos + 1, cerrados, secuencia_actual + '(', secuencias)
        if cerrados < abiertos:
            generar_recursivo(abiertos, cerrados + 1, secuencia_actual + ')', secuencias)
    
    secuencias = []
    generar_recursivo(0, 0, '', secuencias)
    return secuencias

def procesar_casos():

    try:
        while True:
            n = int(input())                
            secuencias = generar_secuencias(n)
            for secuencia in secuencias:
                print(secuencia)
                
    except EOFError:
        return

if __name__ == "__main__":
    procesar_casos()
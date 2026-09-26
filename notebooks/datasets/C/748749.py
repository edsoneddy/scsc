
def generar_parentesis(n):
    resultados = []
    
    def backtrack(secuencia, abiertos, cerrados):
        if len(secuencia) == 2 * n:
            resultados.append(secuencia)
            return
        
        if abiertos < n:
            backtrack(secuencia + "(", abiertos + 1, cerrados)
        
        if cerrados < abiertos:
            backtrack(secuencia + ")", abiertos, cerrados + 1)
    
    backtrack("", 0, 0)
    
    return resultados

try:
    while True:
        entrada = input().strip()
        if not entrada:
            break
        n = int(entrada)
        if 1 <= n <= 10:
            secuencias = generar_parentesis(n)
            for secuencia in secuencias:
                print(secuencia)
except EOFError:
    pass

def generar_parentesis(n):
    """
    Genera todas las secuencias válidas de paréntesis de tamaño 2n
    ordenadas lexicográficamente utilizando una función recursiva.
    """
    resultado = []
    
    def backtrack(abiertos, cerrados, secuencia):
        # Si la secuencia tiene 2n caracteres, es válida y la agregamos al resultado
        if len(secuencia) == 2 * n:
            resultado.append(secuencia)
            return
        
        # Si hay paréntesis abiertos disponibles, los agregamos
        if abiertos < n:
            backtrack(abiertos + 1, cerrados, secuencia + "(")
        
        # Si hay paréntesis cerrados que pueden agregarse, lo hacemos
        if cerrados < abiertos:
            backtrack(abiertos, cerrados + 1, secuencia + ")")
    
    # Llamamos a la función recursiva iniciando con 0 paréntesis abiertos y cerrados
    backtrack(0, 0, "")
    return resultado

def main():
    # Procesar múltiples casos de prueba
    while True:
        try:
            n = int(input())  # Leemos el número de pares de paréntesis
            # Generamos las secuencias válidas de paréntesis
            secuencias = generar_parentesis(n)
            # Imprimimos cada secuencia en una nueva línea
            print("\n".join(secuencias))
        except EOFError:
            break  # Salir del bucle si no hay más entradas

if __name__ == "__main__":
    main()
def generar_parentesis(n):
    """
    Genera todas las secuencias válidas de paréntesis de tamaño 2n
    ordenadas lexicográficamente.
    """
    def backtrack(abiertos, cerrados, actual):
        """
        abiertos: número de paréntesis abiertos disponibles
        cerrados: número de paréntesis cerrados disponibles
        actual: secuencia actual siendo construida
        """
        # Si ya no hay paréntesis por agregar, tenemos una secuencia válida
        if abiertos == 0 and cerrados == 0:
            resultado.append(actual)
            return
            
        # Siempre podemos agregar un paréntesis abierto si nos quedan
        if abiertos > 0:
            backtrack(abiertos - 1, cerrados + 1, actual + "(")
            
        # Solo podemos agregar un paréntesis cerrado si hay alguno abierto
        if cerrados > 0:
            backtrack(abiertos, cerrados - 1, actual + ")")
    
    resultado = []
    # Comenzamos con n paréntesis abiertos disponibles y ninguno cerrado
    backtrack(n, 0, "")
    return resultado

def main():
    # Procesar múltiples casos de prueba
    while True:
        try:
            n = int(input())
            if n == 0:
                break
            secuencias = generar_parentesis(n)
            # Imprimir cada secuencia en una nueva línea
            for secuencia in secuencias:
                print(secuencia)
        except EOFError:
            break

if __name__ == "__main__":
    main()

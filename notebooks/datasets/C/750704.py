def generar_combinaciones_parentesis(tamano):
    """
    Genera todas las combinaciones válidas de paréntesis de tamaño 2*tamano
    ordenadas lexicográficamente.
    """
    def construir_combinacion(par_abiertos, par_cerrados, combinacion_actual):
        """
        par_abiertos: número de paréntesis abiertos restantes
        par_cerrados: número de paréntesis cerrados restantes
        combinacion_actual: secuencia actual siendo construida
        """
        # Si ya no hay paréntesis por agregar, tenemos una combinación válida
        if par_abiertos == 0 and par_cerrados == 0:
            combinaciones.append(combinacion_actual)
            return
            
        # Podemos agregar un paréntesis abierto si aún tenemos disponibles
        if par_abiertos > 0:
            construir_combinacion(par_abiertos - 1, par_cerrados + 1, combinacion_actual + "(")
            
        # Solo podemos agregar un paréntesis cerrado si hay alguno abierto para balancear
        if par_cerrados > 0:
            construir_combinacion(par_abiertos, par_cerrados - 1, combinacion_actual + ")")
    
    combinaciones = []
    # Comenzamos con tamano paréntesis abiertos disponibles y ninguno cerrado
    construir_combinacion(tamano, 0, "")
    return combinaciones

def ejecutar():
    # Procesar múltiples casos de prueba
    while True:
        try:
            tamano = int(input())
            lista_combinaciones = generar_combinaciones_parentesis(tamano)
            # Imprimir cada combinación en una nueva línea
            for combinacion in lista_combinaciones:
                print(combinacion)
        except EOFError:
            break

if __name__ == "__main__":
    ejecutar()

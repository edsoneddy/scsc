def generate_parentheses(n):
    """
    Genera todas las secuencias válidas de paréntesis de tamaño 2n en orden lexicográfico.
    
    Args:
        n (int): Número de pares de paréntesis a generar
    """
    def backtrack(open_count, close_count, current, result):
        """
        Función recursiva que genera las secuencias usando backtracking.
        
        Args:
            open_count (int): Cantidad de paréntesis abiertos utilizados
            close_count (int): Cantidad de paréntesis cerrados utilizados
            current (str): Secuencia actual siendo construida
            result (list): Lista para almacenar todas las secuencias válidas
        """
       
        if len(current) == 2 * n:
            result.append(current)
            return
        if open_count < n:
            backtrack(open_count + 1, close_count, current + '(', result)
            
        if close_count < open_count:
            backtrack(open_count, close_count + 1, current + ')', result)

    result = []
    backtrack(0, 0, '', result)
    
    for seq in result:
        print(seq)
while True:
    try:
        n = int(input())
        generate_parentheses(n)
    except EOFError:
        break
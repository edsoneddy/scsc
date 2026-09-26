def generate_parentheses(n, current="", open_count=0, close_count=0):
    # Si la longitud de la secuencia actual es 2n, se ha generado una secuencia completa
    if len(current) == 2 * n:
        print(current)
        return
    
    # Si se pueden agregar paréntesis abiertos
    if open_count < n:
        generate_parentheses(n, current + "(", open_count + 1, close_count)
    
    # Si se pueden agregar paréntesis cerrados
    if close_count < open_count:
        generate_parentheses(n, current + ")", open_count, close_count + 1)

import sys

# Leer la entrada de varios casos de prueba
for line in sys.stdin:
    n = int(line.strip())
    generate_parentheses(n)
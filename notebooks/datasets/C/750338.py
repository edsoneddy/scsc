# Lista que guarda los números ingresados
numeros = []

# Procesamiento de las operaciones
while True:
    # Leer la instrucción
    instruccion = input().split()
    
    # Si es el comando 'T', terminar el ciclo
    if instruccion[0] == 'T':
        break
    
    # Comando 'S x' - Guardar el número x
    if instruccion[0] == 'S':
        x = int(instruccion[1])
        numeros.append(x)
    
    # Comando 'A' - Imprimir el número más grande
    elif instruccion[0] == 'A':
        if numeros:
            print(max(numeros))
        else:
            print("Error")
    
    # Comando 'R' - Extraer el número más grande
    elif instruccion[0] == 'R':
        if numeros:
            max_num = max(numeros)
            numeros.remove(max_num)
        else:
            print("Error")
    
    # Comando 'I x' - Incrementar el número más grande en x
    elif instruccion[0] == 'I':
        x = int(instruccion[1])
        if numeros:
            max_num = max(numeros)
            # Incrementar solo el primer máximo encontrado
            max_index = numeros.index(max_num)
            numeros[max_index] += x
        else:
            print("Error")
    
    # Comando 'D x' - Decrementar el número más grande en x
    elif instruccion[0] == 'D':
        x = int(instruccion[1])
        if numeros:
            max_num = max(numeros)
            # Decrementar solo el primer máximo encontrado
            max_index = numeros.index(max_num)
            numeros[max_index] -= x
        else:
            print("Error")

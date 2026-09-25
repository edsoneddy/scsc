import sys
input = sys.stdin.read
def procesar_operaciones(operaciones):
    pila = []
    resultados = []
    
    for operacion in operaciones:
        if operacion[0] == 'S':
            _, x = operacion.split()
            pila.append(int(x))
        elif operacion[0] == 'A':
            if pila:
                resultados.append(str(max(pila)))
            else:
                resultados.append("Error")
        elif operacion[0] == 'R':
            if pila:
                pila.remove(max(pila))
            else:
                resultados.append("Error")
        elif operacion[0] == 'I':
            _, x = operacion.split()
            if pila:
                max_val = max(pila)
                pila[pila.index(max_val)] += int(x)
            else:
                resultados.append("Error")
        elif operacion[0] == 'D':
            _, x = operacion.split()
            if pila:
                max_val = max(pila)
                pila[pila.index(max_val)] -= int(x)
            else:
                resultados.append("Error")
        elif operacion[0] == 'T':
            break
    
    return resultados

# Leer la entrada
datos = input().strip().split('\n')
resultados = procesar_operaciones(datos)

# Imprimir los resultados
for resultado in resultados:
    print(resultado)


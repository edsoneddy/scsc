import sys

def procesar_comandos(comandos):
    numeros = []
    resultados = []
    
    for comando in comandos:
        partes = comando.split()
        instruccion = partes[0]
        
        if instruccion == 'S':
            # Guardar el número en la colección
            x = int(partes[1])
            numeros.append(x)
            numeros.sort()  # Ordenamos la lista cada vez que agregamos un elemento para mantener el mayor al final
        
        elif instruccion == 'A':
            # Imprimir el número más grande
            if numeros:
                resultados.append(str(numeros[-1]))  # El mayor número será el último en la lista ordenada
            else:
                resultados.append("Error")
        
        elif instruccion == 'R':
            # Extraer el número más grande
            if numeros:
                numeros.pop(-1)  # Removemos el último elemento (el más grande)
            else:
                resultados.append("Error")
        
        elif instruccion == 'I':
            # Incrementar el número más grande
            if numeros:
                x = int(partes[1])
                maximo = numeros.pop(-1)  # Tomamos el mayor y lo removemos
                numeros.append(maximo + x)  # Agregamos el número incrementado
                numeros.sort()  # Volvemos a ordenar para mantener el mayor al final
            else:
                resultados.append("Error")
        
        elif instruccion == 'D':
            # Decrementar el número más grande
            if numeros:
                x = int(partes[1])
                maximo = numeros.pop(-1)  # Tomamos el mayor y lo removemos
                numeros.append(maximo - x)  # Agregamos el número decrementado
                numeros.sort()  # Volvemos a ordenar para mantener el mayor al final
            else:
                resultados.append("Error")
        
        elif instruccion == 'T':
            # Terminar la entrada
            break
    
    return resultados

# Leer la entrada desde el teclado hasta que se encuentre la instrucción 'T'
comandos = []
while True:
    linea = input().strip()
    comandos.append(linea)
    if linea == 'T':
        break

# Procesar los comandos y mostrar resultados
resultados = procesar_comandos(comandos)
print("\n".join(resultados))

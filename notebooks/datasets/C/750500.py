def procesar_operaciones():
    numeros = []  # Lista para almacenar los números
    
    while True:
        try:
            entrada = input().strip()
            if not entrada:
                continue
                
            partes = entrada.split()
            operacion = partes[0]
            
            if operacion == 'T':
                break
                
            elif operacion == 'S':
                x = int(partes[1])
                numeros.append(x)
                
            elif operacion == 'A':
                if not numeros:
                    print("Error")
                else:
                    print(max(numeros))
                    
            elif operacion == 'R':
                if not numeros:
                    print("Error")
                else:
                    max_num = max(numeros)
                    numeros.remove(max_num)
                    
            elif operacion == 'I':
                if not numeros:
                    print("Error")
                else:
                    x = int(partes[1])
                    max_num = max(numeros)
                    numeros.remove(max_num)
                    numeros.append(max_num + x)
                    
            elif operacion == 'D':
                if not numeros:
                    print("Error")
                else:
                    x = int(partes[1])
                    max_num = max(numeros)
                    numeros.remove(max_num)
                    numeros.append(max_num - x)
                    
        except EOFError:
            break
        except:
            print("Error")

# Ejecutar el programa
if __name__ == "__main__":
    procesar_operaciones()
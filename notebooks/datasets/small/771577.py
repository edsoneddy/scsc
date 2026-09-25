def main():
    collection = []  # Colección de números
    
    while True:
        try:
            command = input().strip()
            
            if not command:
                continue
                
            operation = command[0]
            
            # Terminar la entrada
            if operation == 'T':
                break
                
            # Guardar una copia de un número x
            elif operation == 'S':
                try:
                    value = int(command[2:])
                    collection.append(value)
                except (ValueError, IndexError):
                    print("Error")
                    
            # Imprimir el número más grande
            elif operation == 'A':
                if collection:
                    print(max(collection))
                else:
                    print("Error")
                    
            # Extraer el número más grande
            elif operation == 'R':
                if collection:
                    max_value = max(collection)
                    collection.remove(max_value)
                else:
                    print("Error")
                    
            # Incrementar el número más grande en x
            elif operation == 'I':
                if collection:
                    try:
                        value = int(command[2:])
                        max_index = collection.index(max(collection))
                        collection[max_index] += value
                    except (ValueError, IndexError):
                        print("Error")
                else:
                    print("Error")
                    
            # Decrementar el número más grande en x
            elif operation == 'D':
                if collection:
                    try:
                        value = int(command[2:])
                        max_index = collection.index(max(collection))
                        collection[max_index] -= value
                    except (ValueError, IndexError):
                        print("Error")
                else:
                    print("Error")
                    
            else:
                print("Error")
                
        except EOFError:
            break

if __name__ == "__main__":
    main()
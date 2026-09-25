def convertir_a_bailarina(cadena):
    resultado = []
    mayuscula = True  # Empezamos con mayúscula
    
    for char in cadena:
        if char != ' ':  # Ignorar espacios
            if mayuscula:
                resultado.append(char.upper())
            else:
                resultado.append(char.lower())
            mayuscula = not mayuscula  # Alternar entre mayúscula y minúscula
        else:
            resultado.append(char)  # Mantener los espacios
    
    return ''.join(resultado)

def main():
    n = int(input())
    
    for _ in range(n):
        entrada = input()
        bailarina = convertir_a_bailarina(entrada)
        print(bailarina)

if __name__ == "__main__":
    main()

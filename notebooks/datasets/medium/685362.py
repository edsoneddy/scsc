def hacer_bailarina(cadena):
    resultado = []
    mayuscula = True  # Empezamos con mayúscula
    
    for caracter in cadena:
        if caracter.isalpha():  # Solo transformar letras
            if mayuscula:
                resultado.append(caracter.upper())
            else:
                resultado.append(caracter.lower())
            mayuscula = not mayuscula  # Alternar
        else:
            resultado.append(caracter)  # No transformar, solo agregar
    
    return ''.join(resultado)

def main():
    import sys
    input = sys.stdin.read
    datos = input().splitlines()
    
    T = int(datos[0])
    casos = datos[1:T + 1]
    
    for caso in casos:
        print(hacer_bailarina(caso))

if __name__ == "__main__":
    main()

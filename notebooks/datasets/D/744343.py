def convertir_a_bailarina(cadena):
    if not cadena:
        return ""
                    
    resultado = []
    mayuscula = True
                                
    for char in cadena:
        if char.isalpha():
            if mayuscula:
                resultado.append(char.upper())
            else:
                resultado.append(char.lower())
            mayuscula = not mayuscula
        else:
            resultado.append(char)
                                                                                                                                        
    return ''.join(resultado)

T = int(input())
for _ in range(T):
    cadena = input()
    print(convertir_a_bailarina(cadena))

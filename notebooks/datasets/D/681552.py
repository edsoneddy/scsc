def convertir_bailarina(cadena):
    resultado = ""
    mayuscula = True
    
    for i, char in enumerate(cadena):
        if char.isalpha():
            if i == 0:
                resultado += char.upper()
                mayuscula = not mayuscula 
            else:
                if mayuscula:
                    resultado += char.upper()
                else:
                    resultado += char.lower()
                mayuscula = not mayuscula  
        else:
            resultado += char
    
    return resultado
T = int(input())
for _ in range(T):
    cadena = input()
    print(convertir_bailarina(cadena))

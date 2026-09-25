def es_bailarina(cadena):
    resultado = []
    uppercase = True
    for char in cadena:
        if char.isalpha():  
            if uppercase:
                resultado.append(char.upper())
            else:
                resultado.append(char.lower())
            uppercase = not uppercase
        else:
            resultado.append(char)
    return ''.join(resultado)
T = int(input())
for _ in range(T):
    cadena = input()
    print(es_bailarina(cadena))

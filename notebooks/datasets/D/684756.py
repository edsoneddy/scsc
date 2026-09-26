def hacer_bailarina(cad):
    resultado = ""
    usar_mayuscula = True
    
    for i in cad:
        if i.isalpha():  
            if usar_mayuscula:
                resultado += i.upper()
            else:
                resultado += i.lower()
            usar_mayuscula = not usar_mayuscula
        else:
            resultado += i
    
    return resultado

t = int(input())

for j in range(t):
    cadena = input()
    print(hacer_bailarina(cadena))
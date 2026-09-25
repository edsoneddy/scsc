def es_bailarina(cadena):
    resultado = ""
    mayuscula = True  # Comenzamos con mayúscula
    for letra in cadena:
        if letra.isalpha():
            if mayuscula:
                resultado += letra.upper()
            else:
                resultado += letra.lower()
            mayuscula = not mayuscula
        else:
            resultado += letra  # Conservamos caracteres no alfabéticos
    return resultado
 
# Leer el número de casos de prueba
T = int(input())
 
# Leer y procesar cada caso de prueba
for _ in range(T):
    cadena = input()
    print(es_bailarina(cadena))
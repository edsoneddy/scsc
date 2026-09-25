def a_mayus_minus(texto):
    resultado = []
    mayuscula = True  # La primera letra debe ser mayúscula
    for caracter in texto:
        if caracter.isalpha():  # Solo procesamos letras
            if mayuscula:
                resultado.append(caracter.upper())
            else:
                resultado.append(caracter.lower())
            mayuscula = not mayuscula  
        else:
            resultado.append(caracter) 
    return ''.join(resultado)

casos = int(input())  # Número de casos de prueba
resultados = []
for _ in range(casos):
    linea = input()  # Leer cada cadena
    resultados.append(a_mayus_minus(linea))
for resultado in resultados:
    print(resultado)
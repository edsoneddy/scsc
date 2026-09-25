def cadena_bailarina(cadena):
    resultado = ''
    es_mayuscula = True
    for letra in cadena:
        if letra.isalpha():
            if es_mayuscula:
                resultado += letra.upper()
            else:
                resultado += letra.lower()
            es_mayuscula = not es_mayuscula
        else:
            resultado += letra
    return resultado


m = int(input())


for _ in range(m):
    cadena = input()
    resultado = cadena_bailarina(cadena)
    print(resultado)
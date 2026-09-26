def convertir_a_bailarina(cadena):
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

def main():
    casos = int(input())
    for _ in range(casos):
        cadena = input()
        print(convertir_a_bailarina(cadena))

main()

def revisar(cadena, izq, der):
    while izq < der:
        while izq < der and not cadena[izq].isalnum():
            izq += 1
        while izq < der and not cadena[der].isalnum():
            der -= 1
        if cadena[izq].lower() != cadena[der].lower():
            return False
        izq += 1
        der -= 1
    return True

entrada = input()
if revisar(entrada, 0, len(entrada) - 1):
    print("yes")
else:
    print("no")

from collections import deque

PARES = {")": "(", "]": "[", "}": "{"}

# Revisa la cadena y devuelve la posicion del primer error (o -1 si esta balanceada)
def revisar(cadena):
    pila = deque()
    indice = 0
    while indice < len(cadena):
        ch = cadena[indice]
        if ch in "([{":
            # Guarda el simbolo y su posicion
            pila.append((ch, indice))
        elif ch in PARES:
            if len(pila) == 0:
                return indice
            abierto = pila.pop()[0]
            if abierto != PARES[ch]:
                return indice
        indice += 1
    if len(pila) > 0:
        return pila[-1][1]
    return -1

casos = int(input())
correctos = 0
# Procesa cada caso de prueba
numero = 1
while numero <= casos:
    linea = input().strip()
    error = revisar(linea)
    if error == -1:
        print("Caso", numero, "balanceada")
        correctos = correctos + 1
    else:
        print("Caso", numero, "error en la posicion", error, "->", linea[:error + 1])
    numero += 1
print("Balanceadas:", correctos, "de", casos)

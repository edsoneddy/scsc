from collections import deque

PARES = {")": "(", "]": "[", "}": "{"}

# Revisa la cadena y devuelve la posicion del primer error (o -1 si esta balanceada)
def revisar(cadena, pares):
    pila = deque()
    for indice, ch in enumerate(cadena):
        if ch in "([{":
            # Guarda el simbolo y su posicion
            pila.append((ch, indice))
        elif ch in pares:
            if len(pila) == 0:
                return indice
            abierto, _ = pila.pop()
            if abierto != pares[ch]:
                return indice
    if len(pila) > 0:
        return pila[-1][1]
    return -1

def procesar_caso(numero):
    linea = input().strip()
    error = revisar(linea, PARES)
    if error == -1:
        print("Caso", numero, "balanceada")
        return 1
    else:
        print("Caso", numero, "error en la posicion", error, "->", linea[:error + 1])
        return 0

casos = int(input())
correctos = 0
# Procesa cada caso de prueba
for numero in range(1, casos + 1):
    correctos += procesar_caso(numero)
print("Balanceadas:", correctos, "de", casos)

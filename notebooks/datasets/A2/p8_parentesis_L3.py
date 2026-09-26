from collections import deque

PARES = {}
PARES[")"] = "("
PARES["]"] = "["
PARES["}"] = "{"

# Revisa la cadena y devuelve la posicion del primer error (o -1 si esta balanceada)
def revisar(cadena):
    pila = deque([])
    for indice, ch in enumerate(cadena):
        if ch in "([{":
            # Guarda el simbolo y su posicion
            pila.append((ch, indice))
        elif ch in PARES:
            if len(pila) == 0:
                return indice
            abierto, _ = pila.pop()
            if abierto != PARES[ch]:
                return indice
    if len(pila) > 0:
        return pila[-1][1]
    return -1

correctos = 0
casos = int(input())
# Procesa cada caso de prueba
for numero in range(1, casos + 1):
    linea = str(input()).strip()
    error = revisar(linea)
    if error == -1:
        print("Caso", numero, "balanceada")
        correctos += 1
    else:
        print("Caso", numero, "error en la posicion", error, "->", linea[:error + 1])
print("Balanceadas:", correctos, "de", casos)

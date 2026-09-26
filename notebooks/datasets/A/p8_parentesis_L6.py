from collections import deque

PARES = {")": "(", "]": "[", "}": "{"}

# Revisa la cadena y devuelve la posicion del primer error (o -1 si esta balanceada)
def revisar(cadena):
    pila = deque()
    for indice, ch in enumerate(cadena):
        if ch in "([{":
            # Guarda el simbolo y su posicion
            pila.append((ch, indice))
        elif ch in PARES:
            if not pila:
                return indice
            abierto, _ = pila.pop()
            if not abierto == PARES[ch]:
                return indice
    return pila[-1][1] if len(pila) != 0 else -1

casos = int(input())
correctos = 0
# Procesa cada caso de prueba
for numero in range(1, casos + 1):
    linea = input().strip()
    error = revisar(linea)
    if error < 0:
        print("Caso", numero, "balanceada")
        correctos += 1
    else:
        print("Caso", numero, "error en la posicion", error, "->", linea[:error + 1])
print("Balanceadas:", correctos, "de", casos)

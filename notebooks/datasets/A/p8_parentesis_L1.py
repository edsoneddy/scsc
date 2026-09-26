from collections import deque

PARES = {")":"(", "]":"[", "}":"{"}

# Devuelve el indice del primer error, o -1 si la cadena esta balanceada
def revisar(cadena):
  pila = deque()
  for indice, ch in enumerate(cadena):
    if ch in "([{":
      # Apila el simbolo junto con su indice
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


casos = int(input())
correctos = 0
# Un caso por linea
for numero in range(1, casos+1):
  linea = input().strip()
  error = revisar(linea)
  if error == -1:
    print("Caso", numero, "balanceada")
    correctos += 1
  else:
    print("Caso", numero, "error en la posicion", error,
      "->", linea[:error+1])
print("Balanceadas:", correctos, "de", casos)

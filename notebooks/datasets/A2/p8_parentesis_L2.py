from collections import deque

PAREJAS = {")": "(", "]": "[", "}": "{"}

# Revisa la cadena y devuelve la posicion del primer error (o -1 si esta balanceada)
def buscar_error(texto):
    stack = deque()
    for pos, simbolo in enumerate(texto):
        if simbolo in "([{":
            # Guarda el simbolo y su posicion
            stack.append((simbolo, pos))
        elif simbolo in PAREJAS:
            if len(stack) == 0:
                return pos
            tope, _ = stack.pop()
            if tope != PAREJAS[simbolo]:
                return pos
    if len(stack) > 0:
        return stack[-1][1]
    return -1

t = int(input())
ok = 0
# Procesa cada caso de prueba
for caso in range(1, t + 1):
    entrada = input().strip()
    fallo = buscar_error(entrada)
    if fallo == -1:
        print("Caso", caso, "balanceada")
        ok += 1
    else:
        print("Caso", caso, "error en la posicion", fallo, "->", entrada[:fallo + 1])
print("Balanceadas:", ok, "de", t)

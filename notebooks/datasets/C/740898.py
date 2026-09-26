import sys
def parentesis(text, binaryValue, i, abierto, posibles, maxI):
    if i >= maxI:
        if abierto == 0:
            posibles.append((int(binaryValue, 2),text))
    else:
        # anadir
        if abierto > 0:
            parentesis(text+')', binaryValue+'0', i+1, abierto-1, posibles, maxI)
        # no anadir
        parentesis(text+'(', binaryValue+'1', i+1, abierto+1, posibles, maxI)
        
lineas = sys.stdin.readlines()
for linea in lineas:
    
    entrada = int(linea.strip())
            
    posibles = []
    parentesis('', '', 0, 0, posibles, entrada*2)
    
    sorted_values = [d for d in sorted(posibles, key=lambda x: x[0], reverse=True)]

    for value in sorted_values:
        print(value[1])
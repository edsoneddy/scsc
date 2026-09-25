import sys
numeros = []
def imprimir_max():
    if numeros:
        print(max(numeros))
    else:
        print("Error")

def extraer_max():
    if numeros:
        numeros.remove(max(numeros))
    else:
        print("Error")

def incrementar_max(x):
    if numeros:
        max_num = max(numeros)
        numeros[numeros.index(max_num)] = max_num + x
    else:
        print("Error")

def decrementar_max(x):
    if numeros:
        max_num = max(numeros)
        numeros[numeros.index(max_num)] = max_num - x
    else:
        print("Error")

for i in sys.stdin:
    ope = i.strip()

    if ope == 'T':
        break
    
    operaciones = ope.split()
    tipo_ope = operaciones[0]
    if tipo_ope == 'S':
        numeros.append(int(operaciones[1]))
    elif tipo_ope == 'A':
        imprimir_max()
    elif tipo_ope == 'R':
        extraer_max()
    elif tipo_ope == 'I':
        incrementar_max(int(operaciones[1]))
    elif tipo_ope == 'D':
        decrementar_max(int(operaciones[1]))


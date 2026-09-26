# Lee la lista de numeros desde la entrada
def leer_numeros():
    linea = input()
    valores = []
    for token in linea.split():
        valores.append(int(token))
    return valores

# Ordena por intercambio: compara cada par vecino
def burbuja(arr):
    largo = len(arr)
    cambios = 0
    for pasada in range(largo - 1):
        for k in range(largo - 1 - pasada):
            if arr[k] > arr[k + 1]:
                temp = arr[k]
                arr[k] = arr[k + 1]
                arr[k + 1] = temp
                cambios += 1
    return cambios

entrada = leer_numeros()
print("Original:", entrada)
veces = burbuja(entrada)
print("Ordenada:", entrada)
print("Intercambios:", veces)
# Muestra extremos
if len(entrada) > 0:
    print("Minimo:", entrada[0], "Maximo:", entrada[-1])
else:
    print("Lista vacia")
primera = entrada[:len(entrada) // 2]
print("Primera mitad:", primera)

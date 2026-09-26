# Lee la lista de numeros desde la entrada
def leer_lista():
    texto = input()
    numeros = []
    for parte in texto.split():
        numeros += [int(parte)]
    return numeros

# Ordena por intercambio: compara cada par vecino
def ordenar(lista):
    n = len(lista)
    intercambios = 0
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios = intercambios + 1
            j += 1
        i += 1
    return intercambios

datos = leer_lista()
print("Original:", datos)
total = ordenar(datos)
print("Ordenada:", datos)
print("Intercambios:", total)
# Muestra extremos
if len(datos) > 0:
    print("Minimo:", datos[0], "Maximo:", datos[-1])
else:
    print("Lista vacia")
mitad = datos[:int(len(datos) / 2)]
print("Primera mitad:", mitad)

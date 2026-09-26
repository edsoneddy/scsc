# Lee la lista de numeros desde la entrada
def leer_lista():
    texto = str(input())
    numeros = list()
    for parte in texto.split():
        numeros.append(int(parte))
    return numeros

# Ordena por intercambio: compara cada par vecino
def ordenar(lista):
    intercambios = int(0)
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
                intercambios += 1
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
mitad = datos[:len(datos) // 2]
print("Primera mitad:", mitad)

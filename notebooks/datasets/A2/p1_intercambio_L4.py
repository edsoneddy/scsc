# Lee la lista de numeros desde la entrada
def leer_lista():
    texto = input()
    numeros = []
    for parte in texto.split():
        numeros.append(int(parte))
    return numeros

def intercambiar(lista, j):
    aux = lista[j]
    lista[j] = lista[j + 1]
    lista[j + 1] = aux

# Ordena por intercambio: compara cada par vecino
def ordenar(lista):
    n = len(lista)
    intercambios = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                intercambiar(lista, j)
                intercambios += 1
    return intercambios

def mostrar_extremos(datos):
    if len(datos) > 0:
        print("Minimo:", datos[0], "Maximo:", datos[-1])
    else:
        print("Lista vacia")

datos = leer_lista()
print("Original:", datos)
total = ordenar(datos)
print("Ordenada:", datos)
print("Intercambios:", total)
# Muestra extremos
mostrar_extremos(datos)
mitad = datos[:len(datos) // 2]
print("Primera mitad:", mitad)

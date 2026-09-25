n = int(input())
for casos in range(n):
    palabra = input()
    palabra = palabra.lower()
    listapalabraant = list(palabra)
    palabra = palabra.replace(" ", "")
    listapalabra = list(palabra)
    numletras = len(listapalabra)
    for i in range(0, numletras, 2):
        numero = ord(listapalabra[i])
        if 97 <= numero <= 122:
            numero = numero - 32
            listapalabra[i] = chr(numero)
    for u in range(len(listapalabraant)):
        if listapalabraant[u] == " ":
            listapalabra.insert(u, " ")
    print("".join(listapalabra))

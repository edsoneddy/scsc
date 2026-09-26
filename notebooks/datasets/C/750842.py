import heapq

def ejecutar_comandos(comandos):
    heap_max = []
    salida = []

    for comando in comandos:
        if comando.startswith("S "):
            partes = comando.split(" ")
            valor = int(partes[1])
            heapq.heappush(heap_max, -valor)
        elif comando == "A":
            if heap_max:
                salida.append(str(-heap_max[0]))
            else:
                salida.append("Error")
        elif comando == "R":
            if heap_max:
                heapq.heappop(heap_max)
            else:
                salida.append("Error")
        elif comando.startswith("I "):
            if heap_max:
                partes = comando.split(" ")
                incremento = int(partes[1])
                maximo = -heapq.heappop(heap_max)
                heapq.heappush(heap_max, -(maximo + incremento))
            else:
                salida.append("Error")
        elif comando.startswith("D "):
            if heap_max:
                partes = comando.split(" ")
                decremento = int(partes[1])
                maximo = -heapq.heappop(heap_max)
                heapq.heappush(heap_max, -(maximo - decremento))
            else:
                salida.append("Error")
        elif comando == "T":
            break

    return salida

def principal():
    comandos = []
    while True:
        entrada = input().strip()
        comandos.append(entrada)
        if entrada == "T":
            break

    resultados = ejecutar_comandos(comandos)
    for resultado in resultados:
        print(resultado)

principal()

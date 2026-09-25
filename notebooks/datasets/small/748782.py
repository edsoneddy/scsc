import heapq

def procedimientos(n, heap):
    dato = n[0]
    if(dato == "S"):
        numero = -1* (int((n[1])))
        heapq.heappush(heap, numero)
    elif(dato == "A"):
        if(heap):
            almacenar = heapq.heappop(heap)
            print(-1*almacenar)
            heapq.heappush(heap, almacenar)
        else:
            print("Error")
    elif(dato == "R"):
        if(heap):
            heapq.heappop(heap)
        else:
            print("Error")
    elif(dato == "I"):
        if(heap):
            almacenar = heapq.heappop(heap)
            numero = (int((n[1])))
            sumar = almacenar - numero
            heapq.heappush(heap, sumar)
        else:
            print("Error")
    elif(dato == "D"):
        if(heap):
            almacenar = heapq.heappop(heap)
            numero = (int((n[1])))
            sumar = almacenar + numero
            heapq.heappush(heap, sumar)
        else:
            print("Error")


heap = []
while(True):
    n = list(map(str, input().strip().split()))
    if(n[0] == "T"):
        break
    else:
        procedimientos(n, heap)



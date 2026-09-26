import heapq
def leer_instr():
    cPrioridad =[]
    salidas = []
    while True:
        e = input().strip()
        if e =="T":
            break
        parte = e.split()
        ope = parte[0]

        if ope == "S":
            x = int(parte[1])
            heapq.heappush(cPrioridad,-x)            
        elif ope == "A":
            if cPrioridad:
                salidas.append(-cPrioridad[0])
            else:
                salidas.append("Error")
        elif ope == "R":    
            if cPrioridad:
                heapq.heappop(cPrioridad)
            else:
                salidas.append("Error")
        elif ope == "I":
            if cPrioridad:
                x = int(parte[1])
                max = -heapq.heappop(cPrioridad)
                max += x
                heapq.heappush(cPrioridad, -max)
            else:    
                salidas.append("Error")
        elif ope == "D":
            if cPrioridad:
                x = int(parte[1])
                max = -heapq.heappop(cPrioridad)
                max -= x
                heapq.heappush(cPrioridad, -max)
            else:    
                salidas.append("Error")    
    return salidas
#Main
instr = leer_instr()
for salida in instr:
    print(salida)
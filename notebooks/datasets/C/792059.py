# Leer el año de entrada
año = int(input())

 
es_bisiesto = False

if año % 4 == 0:
     
    if año % 100 == 0:
        
        if año % 400 == 0:
            es_bisiesto = True
         
        else:
            es_bisiesto = False
    
    else:
        es_bisiesto = True
 
else:
    es_bisiesto = False

 
if es_bisiesto:
    print("si")
else:
    print("no")
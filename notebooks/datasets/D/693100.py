casos_de_prueba = int(input())


while casos_de_prueba > 0 : 
    cadena_bailarina = ""
    bandera = True
    cadena  = input()
    longitud = len(cadena)

    for i in cadena  : 
        if i == " " : 
            cadena_bailarina += " "
        elif bandera == True : 
            mayuscula = i.upper()
            cadena_bailarina += mayuscula
            bandera = False
        elif bandera ==  False  : 
            minuscula = i.lower()
            cadena_bailarina += minuscula
            bandera =True
    print(cadena_bailarina)
    
    casos_de_prueba -= 1 
    
    
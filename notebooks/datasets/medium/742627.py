# inicio
n = int(input())  

for i in range(1, n+1):
    c1 = input()  
    c2 = "" 
    sw = 0  #para minus

    #caracter creo
    for k in range(0, len(c1)):
        if c1[k] == ' ':  #espacios
            c2 += ' '
        else:
            if sw == 0:  # si es 0 se agrega espacio ojojojo
                c2 += c1[k].upper()
                sw = 1  
            else:  #miu
                c2 += c1[k].lower()
                sw = 0  

    print(c2)  
# fin
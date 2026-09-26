for _ in range (int(input())):
    numero1=input()
    c=0
    if int(numero1)//10==0:
        print ("0 pasos")
    else:
        while True:
            numero2=eval("*".join(numero1))
            c=c+1
            if numero2//10==0:
                cont=c
                sol=numero2
                break
            numero1=str(numero2)
        print (f"{cont} pasos")
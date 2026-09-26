
def contador(Numero):
    contar=0
    while Numero>=10:  
        multiplicar=1
        while Numero!=0:
            digito=Numero%10
            multiplicar*=digito
            Numero//=10
        contar+=1
        Numero=multiplicar
    return contar

casos=int(input())
for i in range(casos):
    Numero=int(input())
    cantidad_pasos=contador(Numero)
    print(f"{cantidad_pasos} pasos")

t=int(input())
while(t>0):
    char = input()
    v = list(char)
    v1 = []
    t=t-1
    # Alternar entre mayúsculas y minúsculas
    ban = 0
    for i in range(len(v)):
        cod = v[i]
        num = ord(cod)
        if(num!=32):
            if ban == 0:
                # Convertir a mayúscula si es minúscula
                if 'a' <= cod <= 'z':
                    num = num - 32
            else:
                # Convertir a minúscula si es mayúscula
                if 'A' <= cod <= 'Z':
                    num = num + 32
            v1.append(chr(num))
            ban = 1 - ban
        else:
            v1.append(chr(num))
    print(''.join(v1))
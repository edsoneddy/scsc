T = int(input())
for _ in range(T):
    t = input().lower()
    bailarina = []
    cambio = True
    alf = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(len(t)):
        if t[i] == ' ':
            bailarina.append(' ')
        elif t[i] in alf:
            if cambio:                      
                bailarina.append(t[i].upper())
            else:
                bailarina.append(t[i].lower())
            cambio = not cambio

    print(''.join(bailarina))

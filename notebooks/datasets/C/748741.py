#Milan Calixto Calle OInofre v 3.1 okk
def VAMOSS():
    n = []
    
    while True:
        c = input().strip() 
        p = c.split()
        op = p[0]

        if op == "S":
            x = int(p[1])
            n.append(x)
        elif op == "A":
            if n:
                print(max(n))
            else:
                print("Error")
        elif op == "R":
            if n:
                n.remove(max(n))
            else:
                print("Error")
        elif op == "I":
            if n:
                x = int(p[1])
                maxi = max(n)
                n[n.index(maxi)] += x
            else:
                print("Error")
        elif op == "D":
            if n:
                x = int(p[1])
                maxi = max(n)
                n[n.index(maxi)] -= x
            else:
                print("Error")
        elif op == "T":
            break 

VAMOSS()
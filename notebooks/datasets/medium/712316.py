l = int(input())

for e in range(l):
    n = input()
    n1 = ""
    verif = True

    for char in n:
        if char.isalpha():
            if verif:
                n1 += char.upper()
            else:
                n1 += char.lower()
            verif = not verif
        else:
            n1 += char  

    print(n1)
